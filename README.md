# CategoryMatching
Matching GMB categories to Partner Site categories for Synup contest: https://synup.com/contest.txt


There are various ways to get the similarity between text like : Syntactic and other path based, Feature Based Method, Path similarity, Wu and Palmer Semantic Similarity Measure, etc. For category mapping,
the approach that I used is the semantic similarity between sentences using wordnet.


#### What is Semantic?
Semantic means relating to meaning in language or logic. So, Semantic similarity between sentences gives us the meaning and its relatedness.

#### What is Wordnet?
WordNet is a large lexical database of English. Nouns, verbs, adjectives and adverbs are grouped into sets of cognitive synonyms (synsets), each expressing a distinct concept.


#### What is Synset?
Synsets are the synonym sets of the word which are interlinked by means of conceptual-semantic and lexical relations.


#### What is Path similarity?
Calculates the Shortest path distance between synsets. You can read more from [1](Page 4).


#### What is Wu and Palmer Semantic Similarity Measure?
Wu and Palmer defined the similarity measure as words position in the lexical hierarchical structure relative to the position of the most specific common subsumer(root).You can read more from [2]


#### In the First Paper Semantic Similarity is calculated as:

Using lexical database methodology, the similarity is determined by using predefined word hierarchy which has [words,meaning,relationship] with other words stored in a tree like structure.
<br><br> Calculation for Word Similarity:
    1. Path distance between the words
    2. The depth of the subsumer (root) in the hierarchy
    3. Use word corpus to calculate info content of the word
<br><br>Calculation for Sentence Similarity:
    1. sentence->word tokens
    2. calculate : word similarity, sentence similarity, word order similarity
    3. Use lexical database to compare the meaning of the word
    4. form semantic vector for each sent with weights of the word (use info content which has word freq domain wise)
    5. Form order vector (Syntactic similarity between sent) 6. Calculate semantic similarity based on semantic vector and order vec


In the second paper semantic similarity is calculated as: The process followed is: <br></br>
    1. Tagging
    2. Lemma
    3. Wordnet
    4. Process sent pairs
    5. Semantic Sim measures[Shortest Path,Wu&Palmer, Feature]
    6. compare the score

