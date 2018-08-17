'''
This file indexes the lyrics so that the rhymes can be found very quickly
'''



import sys,os
dir = os.path.dirname(__file__)


'''
	This function indexes the lyrics. The index acts like a dictionary where the key is the rhyme and the value is 
	the sentence which the rhyme is in.
'''
def IndexLyrics_Artist(artist):
	index = []
	
	#declare output files
	lyricsFileCompressed = "LyricsCompressed" + ".txt"
	lyricsFileCompressed = os.path.join(dir, "Text", lyricsFileCompressed)  
	indexFile =  artist.capitalize() + "Index" + ".txt"
	indexFile = os.path.join(dir,"Text", indexFile) 
	
	#make a an index for the lyrics
	with open(indexFile, "w") as file:	
		f=open(lyricsFileCompressed)
		lines=f.readlines()
		for x in range(0, len(lines)-1):
			try:
				#store the last word in the line in the index 
				word_list = lines[x].split() 
				index.append(word_list[-1]) 
				file.write(word_list[-1])
				file.write("\n")
			except:
				print("Lyrics skipped because of encoding")	
	
	return index