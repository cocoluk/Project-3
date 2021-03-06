# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print("START*******")

import nltk 
import random

#nltk.download('punkt')

from nltk import word_tokenize,sent_tokenize
from nltk.book import text2

debug = False #True

stuff = []
for x in text2[:151]:
	stuff.append(x)

print (stuff)

# get file from user to make mad lib out of
#if debug:
#	print ("Getting information from file madlib_test.txt...\n")
#tfname = "text2" # need a file with this name in directory


tagged_tokens = nltk.pos_tag(stuff) # gives us a tagged list of tuples
#print("TAGGED TOKENS")
#print(tagged_tokens)
if debug:
	print ("First few tagged tokens are:")
	for tup in tagged_tokens[:151]:
		print (tup)

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective","NNP":"a proper noun"}
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"JJ":.1,"NNP":.1}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = []


for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))


print ("".join(final_words))


print("\n\nEND*******")
