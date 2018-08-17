'''
This file is used to find songs by the specified artirts
'''


import time
import urllib3
#import requests
#import json
import re
from bs4 import BeautifulSoup
import random


'''
	This function returns a list of url's which are url's to songs by the artist
'''
def FindURLs_NLG(artist):
	#construct the url
	mainURL = "https://www.azlyrics.com/"+artist[0]+'/'+artist+".html"
	
	#let the server rest
	rand = random.randint(10, 20);
	time.sleep(rand)
	
	
	# if you want to query the website with requests instead of BeautifulSoup uncomment this code and comment BeautifulSoup code
	'''
	# query the website and return the html to the variable 'page'
	web = urllib3.urlopen(mainURL)
	# parse the html using beautiful soup and store in variable `soup`
	soup = BeautifulSoup(page, 'html.parser')
	'''
	
	'''
	s = requests.Session()
	proxies = {
	  'http': 'http://10.10.1.10:3128',
	  'https': 'http://10.10.1.10:1080',
	}
	web = s.get(mainURL, proxies=proxies)
	soup = BeautifulSoup(web.content)
	'''
	
	
	http = urllib3.PoolManager()

	response = http.request('GET', mainURL)
	soup = BeautifulSoup(response.data)
	
	#using bs4 find_all to find the song lists by the artist 
	songList  = soup.find_all('a', attrs={'target':'_blank'})
	
	URLs = [] #Store the url's in a list
	startText = '/'+artist+'/'
	endText = '.html'
	for i in range(0, len(songList)-1):
		line = str(songList[i])
		#check if the song is produced by the artist or they are featured in it
		if(line.rfind(startText) != -1):
			startIndex = (line.index(startText) + len(artist) + 2)
			endIndex = (line.index(endText))
			song = line[startIndex:endIndex]
			url = "https://www.azlyrics.com/lyrics"+startText+song+endText #construct the url
			URLs.append(url)
		
	return URLs
		




