'''
This file isn't used in the program yet, but it is going to be used to make
a Rhyme Dictionary, where the program will try and put probabilities on
words that could rhyme by learning from the rappers
'''


def RhymeDict_NLG(index):
	
	RhymeDict_NLG = {}
	for i in range(1, len(index)-1):
		
		if(index[i] not in RhymeDict_NLG):
			RhymeDict_NLG[index[i]] = {}
		
		rhymes = RhymeDict_NLG[index[i]]	
		
		if(index[i-1] not in rhymes):
			rhymes[index[i-1]] = 1
		else:
			rhymes[index[i-1]] = rhymes[index[i-1]] + 1
			
		if(index[i+1] not in rhymes):
			rhymes[index[i+1]] = 1
		else:
			rhymes[index[i+1]] = rhymes[index[i+1]] + 1
		
			
		
	return RhymeDict_NLG
			
			
			