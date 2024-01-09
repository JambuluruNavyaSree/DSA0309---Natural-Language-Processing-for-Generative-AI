from nltk.util import ngrams
sentence = "Natural language processing is a field of study focused on the interactions between human language and computers."
words = sentence.split()
bigrams = ngrams(words, 2)
for bigram in bigrams:
    print(bigram)
