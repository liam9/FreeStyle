'''
This file peforms the rapping with the artist and user
'''



import sys,os
dir = os.path.dirname(__file__)
import re
from CreateIndex_Artist import IndexLyrics_Artist
import random
import string 


'''
	This function formats and indexes the artist lyrics. It then creates rhyming classes
	The function matches artist and user rhyming classes
	The function will output a reponse to the users verse
'''
def Rap_Artist(verse):
	
	#remove punctuation 
	verse = re.sub(r'[^\w\s]','',verse)
	#make all characters lower case
	verse = verse.lower()
	
	
	
	try:
		
		artistNumber = 1
		artist = "eminem"
		
		artistNumber = random.randint(1, 8)
		if(artistNumber == 1):
			artist = "eminem"
		if(artistNumber == 2):
			artist = "drdre"
		elif(artistNumber == 3):
			artist = "guccimane"
		elif(artistNumber == 4):
			artist = "drake"
		elif(artistNumber == 5):
			artist = "lilwayne"
		elif(artistNumber == 6):
			artist = "jayz"
		elif(artistNumber == 7):
			artist = "kendricklamar"
		elif(artistNumber == 8):
			artist = "nas"
		

		#create output files
		rhymeClassesFile = "RhymeClasses.txt"
		rhymeClassesFile = os.path.join(dir, "Text", rhymeClassesFile)    
		lyricsFile =  artist.capitalize() + "Lyrics" + ".txt"
		lyricsFile = os.path.join(dir, "Text", lyricsFile)  
		lyricsFileCompressed =  "LyricsCompressed" + ".txt"
		lyricsFileCompressed = os.path.join(dir, "Text", lyricsFileCompressed)  
		indexFile =  artist.capitalize() + "Index" + ".txt"
		indexFile = os.path.join(dir,"Text", indexFile)  
		
		
		#remove blank lines in the lyrics file so the rhymes can be indexed
		with open(lyricsFileCompressed,"w") as file:
			with open(lyricsFile) as f:
				for line in f:
					if not line.isspace():
					   file.write(line)

		
		
		classes = []
		
		#index the lyrics			   
		index = IndexLyrics_Artist(artist)
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
		f=open(lyricsFileCompressed)
		lines=f.readlines()
		responseVerses = []		
		if matchCount != 0:
			for i in range(len(index)):
				if index[i].endswith(classMatch):
					if(word.lower() != index[i].lower()):
						verse = []
						verse.append(lines[i])
						verse.append(lines[i-1])
						verse.append(lines[i+1])
						responseVerses.append(verse)
					
		
		#print a random repsonse verse
		print("\n")
		randChoice_2 = random.randint(1, len(responseVerses))
		for j in range(len(responseVerses[randChoice_2-1])):
				print(responseVerses[randChoice_2-1][j])
		
		return responseVerses[randChoice_2-1]
		'''
		#Print the responseVerses		
		for i in range(len(responseVerses)):
			for j in range(len(responseVerses[i])):
				print(responseVerses[i][j])
		'''
		
	except:
		print("Damn, I got nothing to say")
		output = ["Damn, I got nothing to say"]
		return output
			
	output = ["Damn, I got nothing to say"]
	return output
	
	


