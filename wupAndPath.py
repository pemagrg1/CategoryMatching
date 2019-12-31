import nltk
import numpy as np
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn


def tokenize(q1, q2):
    return nltk.word_tokenize(q1), nltk.word_tokenize(q2)


def posTag(q1, q2):
    return nltk.pos_tag(q1), nltk.pos_tag(q2)


def senselist(word, sentence):
    meanings = {}
    syns = lesk(sentence.split(), word)
    if syns is not None:
        word_syn = syns._name
        # definition = syns.definition()
        meanings[word] = word_syn
        return (word, meanings[word], wn.synset(meanings[word]).definition())
    else:
        return


def lemmaAndSense(tag_q, Sentence):
    sentence_NNVB = []  # nouns and verbs
    sentence_lesk = []  # (word,synset,meaning)

    for index, tagged_word in enumerate(tag_q):
        word = (tagged_word[0])
        tag = (tagged_word[1])
        if 'NN' in tag or 'JJ' in tag or 'VB' in tag:  # "NN" in tag considers all Noun like NN,NNS,NNP same for verb and adjectives
            sentence_NNVB.append(word)

    for word in sentence_NNVB:
        l = senselist(word, Sentence)
        if l is not None:
            sentence_lesk.append(l)
    return sentence_lesk


def computePath(q1, q2):
    R = np.zeros((len(q1), len(q2)))

    for i in range(len(q1)):
        for j in range(len(q2)):
            sim = wn.path_similarity(wn.synset(q1[i][1]), wn.synset(q2[j][1]))
            R[i, j] = sim
    return R


def computeWup(q1, q2):
    R = np.zeros((len(q1), len(q2)))

    for i in range(len(q1)):
        for j in range(len(q2)):
            sim = wn.wup_similarity(wn.synset(q1[i][1]), wn.synset(q2[j][1]))
            R[i, j] = sim
    return R


def overallSim(q1, q2, R):
    sum_X = 0.0
    sum_Y = 0.0

    for i in range(len(q1)):
        max_i = 0.0
        for j in range(len(q2)):
            if R[i, j] > max_i:
                max_i = R[i, j]
        sum_X += max_i

    for i in range(len(q1)):
        max_j = 0.0
        for j in range(len(q2)):
            if R[i, j] > max_j:
                max_j = R[i, j]
        sum_Y += max_j

    if (float(len(q1)) + float(len(q2))) == 0.0:
        return 0.0

    overall = (sum_X + sum_Y) / (2 * (float(len(q1)) + float(len(q2))))

    return overall


def wupAndPathMapping(q1, q2):
    tokens_q1, tokens_q2 = tokenize(q1, q2)
    tag_q1, tag_q2 = posTag(tokens_q1, tokens_q2)

    sentence1Means = lemmaAndSense(tag_q1, q1)
    sentence2Means = lemmaAndSense(tag_q2, q2)

    R1 = computePath(sentence1Means, sentence2Means)
    R2 = computeWup(sentence1Means, sentence2Means)
    R = (R1 + R2) / 2
    return overallSim(sentence1Means, sentence2Means, R)*2



#################################TEST########################
# x = wupAndPathMapping("Cajun Restaurant","Restaurant")
# print(x)