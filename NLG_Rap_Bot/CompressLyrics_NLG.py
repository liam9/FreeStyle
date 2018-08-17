'''
This file is used to put all the artist lyrics into one file with no empty lines
'''



import sys,os
dir = os.path.dirname(__file__)
import string

from Formats_NLG import FormatArtistName_NLG

def CompressLyrics_NLG():

	#create output files
	rhymeClassesFile = "RhymeClasses.txt"
	rhymeClassesFile = os.path.join(dir, "Text", rhymeClassesFile)    
	lyricsFileCompressed =  "LyricsCompressed" + ".txt"
	lyricsFileCompressed = os.path.join(dir, "Text", lyricsFileCompressed)  
	indexFile = "Index" + ".txt"
	indexFile = os.path.join(dir,"Text", indexFile)  

	

	'''
	Remove blank lines in the lyrics file so the rhymes can be indexed
	Put all the lyrics into one file
	'''
	
	with open(lyricsFileCompressed,"w") as file:
		artist_list = ["eminem", "drdre", "guccimane", "drake", "jayz", "lildicky", "kendricklamar", "lilwayne"]
		for artist in artist_list:
			artist = FormatArtistName_NLG(artist)
			lyricsFile =  artist.capitalize() + "Lyrics" + ".txt"
			lyricsFile = os.path.join(dir, "Text", lyricsFile) 
			with open(lyricsFile) as f:
				for line in f:
					if not line.isspace():
					   file.write(line)