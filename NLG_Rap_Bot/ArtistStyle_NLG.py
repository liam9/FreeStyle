'''
This file formats the txt lyrics so the rhymes can be identified within the lyrics
'''


'''
	This function splits lines on the Strings "You", "I", and ',' because with most rap styles 
	these Strings indicate a new rhyme
'''
def ArtistStyle_NLG(artist, Lyrics):
	Phrases = Lyrics.split(",");
	
	for x in range(0, len(Phrases)):
		Phrases[x].splitlines()

	for x in range(0, len(Phrases)):
		Phrases[x].split("I")
			
	for x in range(0, len(Phrases)):
		Phrases[x].split("You")
		
		
	return Phrases
