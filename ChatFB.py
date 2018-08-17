import sys, os

from fbchat import log, Client
from fbchat.models import *


from WebBrowser import OpenWebpage
from ResponseFB import NLGRapBot
from ResponseFB import ArtistRapBot

print("\n")
clientname = input("Enter your Facebook Email: ")
password = input("Enter your Facebook Password: ")

client = Client(clientname, password)
print('Own id: {}'.format(client.uid))
print("\n\n")





def ListAllUsers():
	users = client.fetchAllUsers()
	print(len(users))
	for i in range(len(users)):	
		print(format(users[i].name))
		
def SendMessageToUser(username, message):
	user = client.searchForUsers(username)[0]
	user_name = format(user.name)
	user_uid = format(user.uid)
	print(user_name)
	print(user_uid)
	print("Is user your friend:", format(user.is_friend))
	client.send(Message(text=message), thread_id=user_uid, thread_type=ThreadType.USER)
	
def RapWithUsersUsingNLGBot(username, message):
	user = client.searchForUsers(username)[0]
	user_name = format(user.name)
	user_uid = format(user.uid)
	profilePic_URL = format(user.photo)
	print(user_name)
	print(user_uid)
	print(profilePic_URL)
	OpenWebpage(profilePic_URL)
	print("Is user your friend:", format(user.is_friend))
	client.send(Message(text=message), thread_id=user_uid, thread_type=ThreadType.USER)
	NLGRapBot.Listener(clientname, password)

def RapWithGroupsUsingNLGBot(THREAD_ID, message):
	client.send(Message(text=message), thread_id=THREAD_ID, thread_type=ThreadType.GROUP)
	NLGRapBot.Listener(clientname, password)
	
def RapWithUsersUsingArtistBot(username, message):
	user = client.searchForUsers(username)[0]
	user_name = format(user.name)
	user_uid = format(user.uid)
	profilePic_URL = format(user.photo)
	print(user_name)
	print(user_uid)
	print(profilePic_URL)
	OpenWebpage(profilePic_URL)
	print("Is user your friend:", format(user.is_friend))
	client.send(Message(text=message), thread_id=user_uid, thread_type=ThreadType.USER)
	ArtistRapBot.Listener(clientname, password)
	
def RapWithGroupsUsingArtistBot(THREAD_ID, message):
	client.send(Message(text=message), thread_id=user_uid, thread_type=ThreadType.USER)
	ArtistRapBot.Listener(clientname, password)
	
def OpenUserPhoto(username):
	user = client.searchForUsers(username)[0]
	user_name = format(user.name)
	user_uid = format(user.uid)
	profilePic_URL = format(user.photo)
	print(user_name)
	print(user_uid)
	print(profilePic_URL)
	OpenWebpage(profilePic_URL)

def FetchCurrentThreads():
	# Fetches a list of the 20 top threads you're currently chatting with
	threads = client.fetchThreadList()
	# Fetches the next 10 threads
	threads += client.fetchThreadList(offset=20, limit=10)
	for thread in threads: 
		print(thread)
	
	


def sendMessageToSelf(message):
	client.send(Message(text=message), thread_id=client.uid, thread_type=ThreadType.USER)

option = 1
while(int(option) != 8):
	print("\n")
	print("1)List all messaging contacts  2)Send a message to a user \n 3)Use NLG Rap Bot on users  	4)Use NLG Rap Bot on group chats 	\n	5)Use an Artist Rap Bot on users   6)Use an Artist Rap Bot on group chats   \n	 7)Fetch all your current threads 	8)Exit ")
	option = int(input(" \n Enter option (1-8): "))
	print("\n")
	if(option == 1):
		ListAllUsers()
	elif(option == 2):
		username = input("Enter a user's name: ")
		message = input("Enter a message: ")
		SendMessageToUser(username, message)
	elif(option == 3):
		username = input("Enter a user's name: ")
		message = input("Enter a starting message: ")
		RapWithUsersUsingNLGBot(username, message)
	elif(option == 4):
		try:
			threadID = input("Enter a Thread_ID: ")
			message = input("Enter a starting message: ")
			RapWithGroupsUsingNLGBot(threadID, message)
		except:
			print("Use option 7)Fetch all your current threads")
	elif(option == 5):
		username = input("Enter a user's name: ")
		message = input("Enter a starting message: ")
		RapWithUsersUsingArtistBot(username, message)	
	elif(option == 6):
		try:
			threadID = input("Enter a Thread_ID: ")
			message = input("Enter a starting message: ")
			RapWithGroupsUsingArtistBot(threadID, message)
		except:
			print("Use option 7)Fetch all your current threads")
	elif(option == 7):
		FetchCurrentThreads()
	
		
	
if(option == 8):
	client.logout()
	sys.exit(1)	
	
	
client.logout()

# -*- coding: UTF-8 -*-

