'''
This file generates rap to freestyle with the user 
'''



import sys,os
dir = os.path.dirname(__file__)
import re
import random
import string 

from CreateIndex_NLG import IndexLyrics_NLG
from RhymeDict_NLG import RhymeDict_NLG
from CompressLyrics_NLG import CompressLyrics_NLG
from Ngram_NLG import NgramsReversed

'''
	This function formats and indexes the artist lyrics. It then creates rhyming classes
	The function matches artist and user rhyming classes
	The function will output a reponse to the users verse
'''
def Rap_NLG(verse):
	
	#remove punctuation
	verse = re.sub(r'[^\w\s]','',verse)
	#make all characters lower case
	verse = verse.lower()
	
	#create output files
	rhymeClassesFile = "RhymeClasses.txt"
	rhymeClassesFile = os.path.join(dir, "Text", rhymeClassesFile)    
	lyricsFileCompressed =  "LyricsCompressed" + ".txt"
	lyricsFileCompressed = os.path.join(dir, "Text", lyricsFileCompressed)  
	indexFile = "Index" + ".txt"
	indexFile = os.path.join(dir,"Text", indexFile)  
	
					   
	f=open(lyricsFileCompressed)
	text=f.read()
	f.close()
			   
	classes = []

	#index the lyrics			   
	index = IndexLyrics_NLG()
	with open(rhymeClassesFile,"w") as rhymeFile:
		with open(indexFile,"w") as file:
			for i in range(len(index)):
				end = 2
				if(len(index[i]) > 8):
					end = 6
				elif(len(index[i]) > 7):
					end = 5
				elif(len(index[i]) > 6):
					end = 4
				elif(len(index[i]) > 5):
					end = 3
				else:
					end = 2
				
				#remove punctuation
				for c in string.punctuation:
					index[i] = index[i].replace(c,"")
				
				
				#creating rhyming classes
				rand = random.randint(2, end)
				file.write(index[i] + "\n")
				word_list = index[i]
				rhymeClass = index[i][-rand:]
				classes.append(rhymeClass)
				rhymeFile.write(rhymeClass + "\n")
						

	
		print("\n")
		try:

			
			#Take the last word in the verse
			word_list = verse.split() 
			word = word_list[-1]
			classMatch = ""
			matchCount = 0



			#Match the verse rhyme with the largest possible ryhming class
			for i in range(len(classes)):
					if word.endswith(classes[i]):
						if len(classes[i]) > len(classMatch):
							classMatch = classes[i]
							matchCount = matchCount + 1
						
						
			
			randChoice_1 = 0
			if(matchCount == 0):
				print("No Lyrical matches")
			elif(matchCount > 1):
				randChoice_1 = random.randint(1, matchCount)
				
				
			#Match the artists lyrics with the classMatch
			matches = []
			f=open(lyricsFileCompressed)
			lines=f.readlines()
			responseVerses = []		
			if matchCount != 0:
				for i in range(len(index)):
					if index[i].endswith(classMatch):
						if(word.lower() != index[i].lower()):
							matches.append(index[i])
			
			
			#pick random match to the users rhyme
			randChoice_2 = random.randint(0, len(matches)-1)
			matchChoice = matches[randChoice_2]
			rhymeChoice = matchChoice
		
			
			RhymeClasses = []
			#Find the corresponding index to the rhyme choice
			for i in range(len(index)):
				if index[i] == rhymeChoice:
					if(word.lower() != index[i].lower()):
						rhyme = []
						rhyme.append(index[i])
						rhyme.append(index[i-1])
						rhyme.append(index[i+1])
						RhymeClasses.append(rhyme)
					
					
			#pick a random set of rhymes
			print("\n")
			randChoice_3 = random.randint(0, len(RhymeClasses)-1)
			rhymes = RhymeClasses[randChoice_3]
			NGramSentences = NgramsReversed(text, rhymes, 3)
			
			print("\n")
			for NGramSentence in NGramSentences:
				print(NGramSentence)
			
			print("\n")
			
			
			return NGramSentences
		
		
		except:
			print("Damn, I got nothing to say ")
			output = ["Damn, I got nothing to say "]
			return output
			
		
			
	print("Damn, I got nothing to say")
	output = ["Damn, I got nothing to say"]
	return output
