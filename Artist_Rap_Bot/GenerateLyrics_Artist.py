'''
This file crawls lyrics from a song by an artist
It also formats the lyrics so the lyrics can be read easily
'''



import sys,os
dir = os.path.dirname(__file__)
import time
#import requests
import urllib3
from bs4 import BeautifulSoup
import re
import random

from FindSongs_Artist import FindURLs_Artist
from ArtistStyle_Artist import Style_Artist


'''
	This function crawls the song lyrics, formats the lyrics, and writes the formated lyrics to a file
	It also returns the lyrics as a List
'''
def Generate_Artist(artist):
	
	#specify the outfiles
	lyricsFile =  artist.capitalize() + "Lyrics" + ".txt"
	lyricsFile = os.path.join(dir, "Text", lyricsFile)  


	#get the url
	URLs = FindURLs_Artist(artist)



	print((len(URLs)))


	LyricsList = []
	for k in range(0, len(URLs)-1):

		#Let the server rest
		rand = random.randint(10, 20);
		time.sleep(rand)
		
		# specify the url
		quote_page = URLs[k]
		
		'''
		# query the website and return the html to the variable 'page'
		page = urllib2.urlopen(quote_page)
		# parse the html using beautiful soup and store in variable `soup`
		soup = BeautifulSoup(page, 'html.parser')
		'''
		
		'''
		s = requests.Session()
		proxies = {
			  'http': 'http://10.10.1.10:3128',
			  'https': 'http://10.10.1.10:1080',
			}
		page = s.get(quote_page, proxies=proxies)
		soup = BeautifulSoup(page.content)
		'''
		
		http = urllib3.PoolManager()

		response = http.request('GET', quote_page)
		soup = BeautifulSoup(response.data)


		# Take out the <div> of name and get its value
		name_box = soup.find('div', attrs={'class': 'container main-page'})
		name = name_box.text.strip() # strip() is used to remove starting and trailing


		#Find the lyrics and related songs
		Sections = name.split("if  ( /") 
		Lyrics = Sections[0]

		Sections2 = Sections[1].split("}")
		RelatedSongs = Sections2[1]
		

		#Start processing the Lyrics to the custom rap Style_Artist
		Phrases = ArtistStyle_Artist(artist, Lyrics)



		#Remove strings with round, square brackets, or quotations
		for x in range(0, len(Phrases)):
			brackets = "\[(.*?)\]";
			roundBrackets = "\(([^)]+)\)";
			quoted = '\"(.+?)\"'
			Phrases[x] = re.sub(brackets, "", Phrases[x], 0, flags=0)
			Phrases[x] = re.sub(roundBrackets, "", Phrases[x], 0, flags=0)
			Phrases[x] = re.sub(quoted, "", Phrases[x], 0, flags=0)

		#write the lyrics to a file
		with open(lyricsFile, "a") as file:	
			for x in range(0, len(Phrases)-1):
				try:
					#line = str(Phrases[x])
					file.write(Phrases[x])
				except:
					print("Lyrics skipped because of encoding")		
				
					
		
		#store the lyrics in a list
		LyricsList.append(Phrases[x])
	
	

	return LyricsList

		



	

