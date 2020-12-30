import numpy as np
import pandas as pd

from classicML import CLASSICML_LOGGER
from classicML.backend import tree
from classicML.backend import get_pruner


class DecisionTreeClassifier(object):
    """决策树分类器.

    Attributes:
        attribute_name: list of name, default=None,
            属性的名称.
        tree: classicML.backend.tree._TreeNode实例,
            生成的决策树.
        criterion: {'gain', 'gini', 'entropy'}, default='gain',
            决策树学习的划分方式.
        generator: classicML.backend.tree.DecisionTreeGenerator实例,
            生成决策树的实现算法.
        pruner: classicML.backend.tree.Pruner实例,
            决策树的剪枝器.
    """
    def __init__(self, attribute_name=None):
        """初始化决策树.

        Arguments:
             attribute_name: list of name, default=None,
                属性的名称.
        """
        super(DecisionTreeClassifier, self).__init__()
        self.attribute_name = attribute_name

        self.tree = None
        self.criterion = None
        self.generator = None
        self.pruner = None

    def compile(self, criterion='gain', pruning=None):
        """编译决策树, 配置训练时使用的超参数.

        Arguments:
            criterion: {'gain', 'gini', 'entropy'}, default='gain',
                决策树学习的划分方式.
            pruning: {None, 'pre', 'post'}, default=None,
                是否对决策树进行剪枝操作.

        Raises:
            AttributeError: 参数错误.
        """
        if criterion not in ('gain', 'gini', 'entropy'):
            CLASSICML_LOGGER.error('请检查你使用的划分方式')
            raise AttributeError('参数错误')
        if pruning not in (None, 'pre', 'post'):
            CLASSICML_LOGGER.error('请检查你输入的操作名称')
            raise AttributeError('参数错误')

        self.criterion = criterion
        self.generator = tree.generators.DecisionTreeGenerator(criterion=self.criterion)
        self.pruner = get_pruner(pruning=pruning)

    def fit(self, x, y, x_validation=None, y_validation=None):
        """训练决策树分类器.

        Arguments:
            x: numpy.ndarray or pandas.DataFrame, array-like,
                特征数据.
            y: numpy.ndarray or pandas.DataFrame, array-like,
                标签.
            x_validation: numpy.ndarray or pandas.DataFrame, array-like,
                剪枝使用的验证特征数据.
            y_validation: numpy.ndarray or pandas.DataFrame, array-like,
                剪枝使用的验证标签.

        Returns:
            DecisionTreeClassifier实例.

        Raises:
            AttributeError: 没有验证集.
        """
        if isinstance(x, np.ndarray) and self.attribute_name is None:
            CLASSICML_LOGGER.warn("属性名称缺失, 请使用pandas.DataFrame; 或检查 self.attributes_name")
        if (self.pruner is not None) and (x_validation is None or y_validation is None):
            CLASSICML_LOGGER.error("没有验证集, 无法对决策树进行剪枝")
            raise AttributeError('没有验证集')

        # 为特征数据添加属性信息.
        x = pd.DataFrame(x, columns=self.attribute_name)
        x.reset_index(drop=True, inplace=True)
        self.generator._x = x

        y = pd.Series(y)
        y.reset_index(drop=True, inplace=True)

        # 为验证数据添加属性信息.
        if x_validation is not None:
            x_validation = pd.DataFrame(x_validation, columns=self.attribute_name)
            x_validation.reset_index(drop=True, inplace=True)

            y_validation = pd.Series(y_validation)
            y_validation.reset_index(drop=True, inplace=True)

        # 生成决策树分类器.
        self.tree = self.generator(x, y)

        # 进行剪枝.
        if self.pruner:
            self.tree = self.pruner(x, y, x_validation, y_validation, self.tree)

        return self

    def predict(self, x):
        """使用决策树分类器进行预测.

        Arguments:
            x: numpy.ndarray or pandas.DataFrame, array-like,
                特征数据.

        Returns:
            DecisionTreeClassifier预测的结果.

        Raises:
            ValueError: 模型没有训练的错误.
        """
        if self.tree is None:
            CLASSICML_LOGGER.error('模型没有训练')
            raise ValueError('你必须先进行训练')

        # 修正数据类型.
        if isinstance(x, list):
            x = np.expand_dims(x, axis=0)
        elif isinstance(x, pd.DataFrame):
            x = x.values
        elif isinstance(x, pd.Series):
            x = np.expand_dims(x.values, axis=0)

        y_pred = list()
        for feature in x:
            y_pred.append(self._predict(feature, self.tree))

        return y_pred

    def _predict(self, x, decision_tree):
        """通过递归决策树预测结果.

        Arguments:
            x: numpy.ndarray, 特征数据.
            decision_tree: classicML.backend.tree._TreeNode, 决策树实例.
        """
        if decision_tree.leaf:
            return decision_tree.category

        if decision_tree.continuous:
            if x[decision_tree.feature_index] >= decision_tree.dividing_point:
                return self._predict(x, decision_tree.subtree['>= {:.3f}'.format(decision_tree.dividing_point)])
            else:
                return self._predict(x, decision_tree.subtree['< {:.3f}'.format(decision_tree.dividing_point)])
        else:
            return self._predict(x, decision_tree.subtree[x[decision_tree.feature_index]])