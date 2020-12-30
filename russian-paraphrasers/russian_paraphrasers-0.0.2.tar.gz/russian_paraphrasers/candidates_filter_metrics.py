from difflib import SequenceMatcher
from collections import defaultdict
from scipy.spatial import distance
import logging
import nltk

logger = logging.getLogger(__name__)


def range_candidates(sentences, sent, smodel, top_k=3, threshold=0.9):
    """
    Range all possible candidates
    :param sentences: candidates
    :param sent: origin sentence reference
    :param smodel: sentence transformer model
    :param top_k: 3
    :param threshold: threshold for cosine similarity score
    :return: list: top k best candidates
    """
    sentences = list(set(sentences))

    try:
        sentence_embeddings = smodel.encode(sentences)
        origin_emb = smodel.encode([sent])
        best_cands = []
        for sentence, embedding in zip(sentences, sentence_embeddings):
            if sent not in sentence:
                if SequenceMatcher(None, sent, sentence).ratio() < 0.95:
                    score = 1 - distance.cosine(embedding, origin_emb)
                    if score >= threshold:
                        if score != 1.0:
                            if [score, sentence] not in best_cands:
                                best_cands.append([score, sentence])
        hypothesis = sorted(best_cands)[:top_k]
        hypothesis = list([val for [_, val] in hypothesis])
    except Exception as e:
        logger.warning("Can't measure embeddings scores. Error: " + str(e))
        cands = []
        for sentence in sentences:
            if sent not in sentence:
                if SequenceMatcher(None, sent, sentence).ratio() < 0.95:
                    cands.append(sentence)
        hypothesis = list(set(cands))[:top_k]
    return hypothesis


def get_scores(ngeval, best_candidates, sentence):
    """

    :param ngeval:
    :param best_candidates:
    :param sentence:
    :return:
    """
    average_metrics = defaultdict(list)
    if best_candidates:
        for hyp in best_candidates:
            metrics_dict = ngeval.compute_individual_metrics([sentence], hyp)
            for key, value in metrics_dict.items():
                average_metrics[key].append(value)
    metrics = {}
    for key, value in average_metrics.items():
        metrics[key] = sum(value)/len(value)
    return metrics


def check_input(sentence):
    warning = None
    if len(sentence) <= 7:
        warning = "Your sentence is too short. The results can be strange."
    sentences = nltk.sent_tokenize(sentence)
    if len(sentences) > 1:
        warning = "There are more than one sentence! We split it and paraphrase separately."
    return warning, sentences
