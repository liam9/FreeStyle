'''
	This is the main file
	It is used to call Generate_NLG(artist) which Generate_NLGs the lyrics
	It is also used to call Rap_NLG() which freestyles with the user
'''

import os, sys
dir = os.path.dirname(__file__)


#GenerateLyrics_NLG and CompressLyrics_NLG are used to produce text files for Rap_NLG
from GenerateLyrics_NLG import Generate_NLG
from CompressLyrics_NLG import CompressLyrics_NLG

#Rap_NLG is used to Rap_NLG with the user
from Rap_NLG import Rap_NLG


if __name__ == "__main__":

	Rap_NLG()


	''' 
	#pass an artist name with no capitals or spaces to Generate_NLG(artist) to include another Rap_NLG artist
	artist = "snoopdogg"
	Generate_NLG(artist)
	'''


	'''
	CompressLyrics_NLG()
	'''



