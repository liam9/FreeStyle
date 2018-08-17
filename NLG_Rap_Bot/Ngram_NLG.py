'''
This file generates rap using NLG and n-grams
'''


import math
import random
import re
#from nltk.model import NgramModel

'''
returns a weighted choice when passed the n-gram choices
'''
def weighted_choice(choices):
   total = sum(w for c, w in choices)
   r = random.uniform(0, total)
   lower = 0
   for c, w in choices:
      if lower + w > r:
         return c
      lower += w

	  
'''
Generates ngram dictionary given all the words and n = size of gram
'''
def generateNgram(words, n):
    gram = dict()

    # Some helpers to keep us crashing the PC for now
    assert n > 0 and n < 100
	
	
    # Populate N-gram dictionary
    for i in range(len(words)-(n-1)):
        key = tuple(words[i:i+n])
        if key  in gram:
            gram[key] += 1
        else:
            gram[key] = 1

    # Turn into a list of (word, count) sorted by count from most to least
    gram = sorted(list(gram.items()), key=lambda __count: -__count[1])
    return gram


'''
Generates n-grams sentences given the rhyming words. 
A usual n-gram sentence generates the sentence from left to right.
NgramsReversed generates the sentence right to left
'''		
def NgramsReversed(text, rhymes, n):
	text = re.sub("([^\s\w]|_)+", "", text) #text is the full text of all lyrics
	words = re.split('\\s+', text.lower())
	
	# Generate ngram list
	ngram = generateNgram(words, n) # n = the type of n-gram (ex. 3-gram, 4-gram, or 5-gram)

	
	NGramSentences = []
	# Generate sentences with the rhymes
	for word in rhymes:
		NGramSentences.append(getNGramSentenceRandomReversed(ngram, word, n, 10))
	return NGramSentences

'''
Generates an n-gram sentence given the rhyming word. 
Generates the n-gram sentence starting at the 
ending rhyme and working backwards through the sentence.
A usual n-gram sentence generates the sentence from left to right.
'''
def getNGramSentenceRandomReversed(gram, word, n, j = 10):
	NGramSentence = ""
	for i in range(j):
		NGramSentence = word + " " + NGramSentence
		# Get all possible elements ((first word, second word), frequency)
		choices = [element for element in reversed(gram) if element[0][n-1] == word]
		if not choices:
			break

		# Choose a pair with weighted probability from the choice list
		word = weighted_choice(choices)[1]
		
	return NGramSentence

