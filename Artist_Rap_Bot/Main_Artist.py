'''
	This is the main file
	It is used to call Generate_Artist(artist) which Generate_Artists the lyrics
	It is also used to call Rap_Artist() which freestyles with the user
'''


from Generate_Artist import Generate_Artist
from Rap_Artist import Rap_Artist

if __name__ == "__main__":

	Rap_Artist()


	'''
	#pass an artist name with no capitals or spaces to Generate_Artist(artist) to include another Rap_Artist artist
	artist = "guccimane"
	Generate_Artist(artist)
	'''

	
