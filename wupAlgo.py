"""
WU and Palmer Similarity
"""
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn


def penn_to_wn(tag):
    """ Convert between a Penn Treebank tag to a simplified Wordnet tag """
    if tag.startswith('N'):
        return 'n'

    if tag.startswith('V'):
        return 'v'

    if tag.startswith('J'):
        return 'a'

    if tag.startswith('R'):
        return 'r'

    return None


def tagged_to_synset(word, tag):
    wn_tag = penn_to_wn(tag)
    if wn_tag is None:
        return None

    try:
        return wn.synsets(word, wn_tag)[0]
    except:
        return None

def wup_similarity(sentence1, sentence2):
    """ compute the sentence similarity using Wordnet """
    # Tokenize and tag
    sentence1 = pos_tag(word_tokenize(sentence1))
    sentence2 = pos_tag(word_tokenize(sentence2))

    # Get the synsets for the tagged words
    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]

    # Filter out the Nones
    synsets1 = [ss for ss in synsets1 if ss]
    synsets2 = [ss for ss in synsets2 if ss]
    score, count = 0, 0

    # For each word in the first sentence
    for synset in synsets1:
        # Get the similarity value of the most similar word in the other sentence
        best_score = 0
        for ss in synsets2:
            try:
                s = synset.wup_similarity(ss)
                if s is not None:
                    if s > best_score:
                        best_score = s
            except Exception as e:
                print()
        # best_score = max([synset.path_similarity(ss) for ss in synsets2])
        # Check that the similarity could have been computed
        if best_score > 0:
            score = score + best_score
            count = count + 1

    # Average the value
    if count == 0:
        count = 1
    score = score / count
    return score

#################################TEST######################
# print (wup_similarity("Cajun Restaurant","Restaurant"))
# print ("Cajun restaurant".title())