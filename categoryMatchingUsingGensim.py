import numpy as np
from scipy import spatial
import gensim


model = ""
index2word_set = set(model.wv.index2word)

def avg_feature_vector(sentence, model, num_features, index2word_set):
    words = sentence.split()
    feature_vec = np.zeros((num_features, ), dtype='float32')
    n_words = 0
    for word in words:
        if word in index2word_set:
            n_words += 1
            feature_vec = np.add(feature_vec, model[word])
    if (n_words > 0):
        feature_vec = np.divide(feature_vec, n_words)
    return feature_vec

s1_afv = avg_feature_vector('this is a sentence', model=model, num_features=300, index2word_set=index2word_set)
s2_afv = avg_feature_vector('this is also sentence', model=model, num_features=300, index2word_set=index2word_set)
sim = 1 - spatial.distance.cosine(s1_afv, s2_afv)
print(sim)

#load word2vec model, here GoogleNews is used
model = gensim.models.KeyedVectors.load_word2vec_format('../GoogleNews-vectors-negative300.bin', binary=True)
#two sample sentences
s1 = 'the first sentence'
s2 = 'the second text'

#calculate distance between two sentences using WMD algorithm
distance = model.wmdistance(s1, s2)

print ('distance = %.3f' % distance)


distance = model.wv.n_similarity(s1.lower().split(), s2.lower().split())
