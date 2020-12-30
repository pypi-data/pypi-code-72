
from typing import Dict, Tuple
from inspect import signature

import tensorflow as tf
import transformers

from .modeling import MultiModalBertModel
from .params import BaseParams
from .top import (Classification, MultiLabelClassification, PreTrain,
                  Seq2Seq, SequenceLabel, MaskLM)
from .utils import get_embedding_table_from_model, get_transformer_main_model


def variable_summaries(var, name):
    """Attach a lot of summaries to a Tensor (for TensorBoard visualization)."""
    with tf.compat.v1.name_scope(name):
        mean = tf.reduce_mean(input_tensor=var)
        tf.compat.v1.summary.scalar('mean', mean)
        with tf.compat.v1.name_scope('stddev'):
            stddev = tf.sqrt(tf.reduce_mean(
                input_tensor=tf.square(var - mean)))
        tf.compat.v1.summary.scalar('stddev', stddev)
        tf.compat.v1.summary.scalar('max', tf.reduce_max(input_tensor=var))
        tf.compat.v1.summary.scalar('min', tf.reduce_min(input_tensor=var))
        tf.compat.v1.summary.histogram('histogram', var)


@tf.function
def filter_loss(loss, features, problem):

    if tf.reduce_mean(input_tensor=features['%s_loss_multiplier' % problem]) == 0:
        return_loss = 0.0
    else:
        return_loss = loss

    return return_loss


class BertMultiTaskBody(tf.keras.Model):
    """Model to extract bert features and dispatch corresponding rows to each problem_chunk.

    for each problem chunk, we extract corresponding features
    and hidden features for that problem. The reason behind this
    is to save computation for downstream processing.
    For example, we have a batch of two instances and they're from
    problem a and b respectively:
    Input:
    [{'input_ids': [1,2,3], 'a_loss_multiplier': 1, 'b_loss_multiplier': 0},
     {'input_ids': [4,5,6], 'a_loss_multiplier': 0, 'b_loss_multiplier': 1}]
    Output:
    {
      'a': {'input_ids': [1,2,3], 'a_loss_multiplier': 1, 'b_loss_multiplier': 0}
      'b': {'input_ids': [4,5,6], 'a_loss_multiplier': 0, 'b_loss_multiplier': 1}
    }

    """

    def __init__(self, params: BaseParams, name='BertMultiTaskBody'):
        super(BertMultiTaskBody, self).__init__(name=name)
        self.params = params
        self.bert = MultiModalBertModel(params=self.params)
        if self.params.custom_pooled_hidden_size:
            self.custom_pooled_layer = tf.keras.layers.Dense(
                self.params.custom_pooled_hidden_size, activation=tf.keras.activations.selu)
        else:
            self.custom_pooled_layer = None

    @tf.function
    def get_features_for_problem(self, features, hidden_feature, problem, mode):
        # get features with ind == 1
        if mode == tf.estimator.ModeKeys.PREDICT:
            feature_this_round = features
            hidden_feature_this_round = hidden_feature
        else:
            multiplier_name = '%s_loss_multiplier' % problem

            record_ind = tf.where(tf.cast(
                tf.squeeze(features[multiplier_name]), tf.bool))

            hidden_feature_this_round = {}
            for hidden_feature_name in hidden_feature:
                if hidden_feature_name != 'embed_table':
                    hidden_feature_this_round[hidden_feature_name] = tf.squeeze(tf.gather(
                        hidden_feature[hidden_feature_name], record_ind, axis=0
                    ), axis=1)
                    hidden_feature_this_round[hidden_feature_name].set_shape(
                        hidden_feature[hidden_feature_name].shape.as_list())
                else:
                    hidden_feature_this_round[hidden_feature_name] = hidden_feature[hidden_feature_name]

            feature_this_round = {}
            for features_name in features:
                feature_this_round[features_name] = tf.gather_nd(
                    features[features_name],
                    record_ind)

        return feature_this_round, hidden_feature_this_round

    def call(self, inputs: Dict[str, tf.Tensor],
             mode: str) -> Tuple[Dict[str, Dict[str, tf.Tensor]], Dict[str, Dict[str, tf.Tensor]]]:
        _ = self.bert(inputs, mode == tf.estimator.ModeKeys.TRAIN)

        # extract bert hidden features
        inputs['model_input_mask'] = self.bert.get_input_mask()
        inputs['model_token_type_ids'] = self.bert.get_token_type_ids()

        hidden_feature = {}
        for logit_type in ['seq', 'pooled', 'all', 'embed', 'embed_table']:
            if logit_type == 'seq':
                # tensor, [batch_size, seq_length, hidden_size]
                hidden_feature[logit_type] = self.bert.get_sequence_output()
            elif logit_type == 'pooled':
                # tensor, [batch_size, hidden_size]
                hidden_feature[logit_type] = self.bert.get_pooled_output()
                if self.custom_pooled_layer:
                    hidden_feature[logit_type] = self.custom_pooled_layer(
                        hidden_feature[logit_type])
            elif logit_type == 'all':
                # list, num_hidden_layers * [batch_size, seq_length, hidden_size]
                hidden_feature[logit_type] = self.bert.get_all_encoder_layers()
            elif logit_type == 'embed':
                # for res connection
                hidden_feature[logit_type] = self.bert.get_embedding_output()
            elif logit_type == 'embed_table':
                hidden_feature[logit_type] = self.bert.get_embedding_table()

        # for each problem chunk, we extract corresponding features
        # and hidden features for that problem. The reason behind this
        # is to save computation for downstream processing.
        # For example, we have a batch of two instances and they're from
        # problem a and b respectively:
        # Input:
        # [{'input_ids': [1,2,3], 'a_loss_multiplier': 1, 'b_loss_multiplier': 0},
        #  {'input_ids': [4,5,6], 'a_loss_multiplier': 0, 'b_loss_multiplier': 1}]
        # Output:
        # {
        #   'a': {'input_ids': [1,2,3], 'a_loss_multiplier': 1, 'b_loss_multiplier': 0}
        #   'b': {'input_ids': [4,5,6], 'a_loss_multiplier': 0, 'b_loss_multiplier': 1}
        # }
        features = inputs
        return_feature = {}
        return_hidden_feature = {}

        for problem_dict in self.params.run_problem_list:
            for problem in problem_dict:
                if self.params.task_transformer:
                    # hidden_feature = task_tranformer_hidden_feature[problem]
                    raise NotImplementedError

                if len(self.params.run_problem_list) > 1:
                    feature_this_round, hidden_feature_this_round = self.get_features_for_problem(
                        features, hidden_feature, problem, mode)
                else:
                    feature_this_round, hidden_feature_this_round = features, hidden_feature

                if self.params.label_transfer and self.params.grid_transformer:
                    raise ValueError(
                        'Label Transfer and grid transformer cannot be enabled in the same time.'
                    )

                if self.params.grid_transformer:
                    raise NotImplementedError
                return_hidden_feature[problem] = hidden_feature_this_round
                return_feature[problem] = feature_this_round
        return return_feature, return_hidden_feature


class BertMultiTaskTop(tf.keras.Model):
    """Model to create top layer, aka classification layer, for each problem.
    """

    def __init__(self, params: BaseParams, name='BertMultiTaskTop', input_embeddings: tf.Tensor = None):
        super(BertMultiTaskTop, self).__init__(name=name)
        self.params = params

        problem_type_layer = {
            'seq_tag': SequenceLabel,
            'cls': Classification,
            'seq2seq_tag': Seq2Seq,
            'seq2seq_text': Seq2Seq,
            'multi_cls': MultiLabelClassification,
            'pretrain': PreTrain,
            'masklm': MaskLM
        }
        problem_type_layer.update(self.params.top_layer)
        self.top_layer_dict = {}
        for problem_dict in self.params.run_problem_list:
            for problem in problem_dict:
                problem_type = self.params.problem_type[problem]
                # some layers has different signatures, assign inputs accordingly
                layer_signature_name = signature(
                    problem_type_layer[problem_type].__init__).parameters.keys()
                inputs_kwargs = {
                    'params': self.params,
                    'problem_name': problem
                }
                for signature_name in layer_signature_name:
                    if signature_name == 'input_embeddings':
                        inputs_kwargs.update(
                            {signature_name: input_embeddings})

                self.top_layer_dict[problem] = problem_type_layer[problem_type](
                    **inputs_kwargs)

    def call(self,
             inputs: Tuple[Dict[str, Dict[str, tf.Tensor]], Dict[str, Dict[str, tf.Tensor]]],
             mode: str) -> Dict[str, tf.Tensor]:
        features, hidden_feature = inputs
        return_dict = {}

        for problem_dict in self.params.run_problem_list:
            for problem in problem_dict:
                feature_this_round = features[problem]
                hidden_feature_this_round = hidden_feature[problem]
                problem_type = self.params.problem_type[problem]

                # if pretrain, return pretrain logit
                if problem_type == 'pretrain':
                    pretrain = self.top_layer_dict[problem]
                    return_dict[problem] = pretrain(
                        (feature_this_round, hidden_feature_this_round), mode)
                    return return_dict

                if self.params.label_transfer and self.params.grid_transformer:
                    raise ValueError(
                        'Label Transfer and grid transformer cannot be enabled in the same time.'
                    )

                with tf.name_scope(problem):
                    layer = self.top_layer_dict[problem]

                    return_dict[problem] = layer(
                        (feature_this_round, hidden_feature_this_round), mode)

        if self.params.augument_mask_lm and mode == tf.estimator.ModeKeys.TRAIN:
            raise NotImplementedError
            # try:
            #     mask_lm_top = MaskLM(self.params)
            #     return_dict['augument_mask_lm'] = \
            #         mask_lm_top(features,
            #                     hidden_feature, mode, 'dummy')
            # except ValueError:
            #     pass
        return return_dict


class BertMultiTask(tf.keras.Model):
    def __init__(self, params: BaseParams, name='BertMultiTask') -> None:
        super(BertMultiTask, self).__init__(name=name)
        self.params = params
        # initialize body model, aka transformers
        self.body = BertMultiTaskBody(params=self.params)
        # mlm might need word embedding from bert
        # build sub-model
        _ = get_embedding_table_from_model(self.body.bert.bert_model)
        main_model = get_transformer_main_model(self.body.bert.bert_model)
        # input_embeddings = self.body.bert.bert_model.bert.embeddings
        input_embeddings = main_model.embeddings
        self.top = BertMultiTaskTop(
            params=self.params, input_embeddings=input_embeddings)

    def call(self, inputs, mode=tf.estimator.ModeKeys.TRAIN):
        feature_per_problem, hidden_feature_per_problem = self.body(
            inputs, mode)
        pred_per_problem = self.top(
            (feature_per_problem, hidden_feature_per_problem), mode)
        return pred_per_problem

    def compile(self):
        super(BertMultiTask, self).compile()
        logger = tf.get_logger()
        logger.info('Initial lr: {}'.format(self.params.lr))
        logger.info('Train steps: {}'.format(self.params.train_steps))
        logger.info('Warmup steps: {}'.format(self.params.num_warmup_steps))
        self.optimizer, self.lr_scheduler = transformers.optimization_tf.create_optimizer(
            init_lr=self.params.lr,
            num_train_steps=self.params.train_steps,
            num_warmup_steps=self.params.num_warmup_steps,
            weight_decay_rate=0.01
        )
        self.mean_acc = tf.keras.metrics.Mean(name='mean_acc')

    def train_step(self, data):

        with tf.GradientTape() as tape:
            # Forward pass
            _ = self(data, mode=tf.estimator.ModeKeys.TRAIN)
            # gather losses from all problems
            loss_dict = {'{}_loss'.format(problem_name): tf.reduce_sum(top_layer.losses) for problem_name,
                         top_layer in self.top.top_layer_dict.items()}
            # metric_dict = {'{}_metric'.format(problem_name): tf.reduce_mean(top_layer.metrics) for problem_name,
            #                top_layer in self.top.top_layer_dict.items()}
            metric_dict = {m.name: m.result() for m in self.metrics}
        # Compute gradients
        trainable_vars = self.trainable_variables
        gradients = tape.gradient(self.losses, trainable_vars)

        # Update weights
        self.optimizer.apply_gradients(zip(gradients, trainable_vars))

        self.mean_acc.update_state(
            [v for n, v in metric_dict.items() if n != 'mean_acc'])

        return_dict = metric_dict
        return_dict.update(loss_dict)
        return_dict[self.mean_acc.name] = self.mean_acc.result()

        # Return a dict mapping metric names to current value.
        # Note that it will include the loss (tracked in self.metrics).
        return return_dict

    def test_step(self, data):
        """The logic for one evaluation step.

        This method can be overridden to support custom evaluation logic.
        This method is called by `Model.make_test_function`.

        This function should contain the mathemetical logic for one step of
        evaluation.
        This typically includes the forward pass, loss calculation, and metrics
        updates.

        Configuration details for *how* this logic is run (e.g. `tf.function` and
        `tf.distribute.Strategy` settings), should be left to
        `Model.make_test_function`, which can also be overridden.

        Arguments:
        data: A nested structure of `Tensor`s.

        Returns:
        A `dict` containing values that will be passed to
        `tf.keras.callbacks.CallbackList.on_train_batch_end`. Typically, the
        values of the `Model`'s metrics are returned.
        """

        y_pred = self(data, mode=tf.estimator.ModeKeys.EVAL)
        # Updates stateful loss metrics.
        self.compiled_loss(
            None, y_pred, None, regularization_losses=self.losses)

        self.compiled_metrics.update_state(None, y_pred, None)

        # get metrics to calculate mean
        m_list = []
        for metric in self.metrics:
            if 'mean_acc' in metric.name:
                continue
            if 'acc' in metric.name:
                m_list.append(metric.result())

            if 'f1' in metric.name:
                m_list.append(metric.result())

        self.mean_acc.update_state(
            m_list)
        return {m.name: m.result() for m in self.metrics}

    def predict_step(self, data):
        return self(data, mode=tf.estimator.ModeKeys.PREDICT)
