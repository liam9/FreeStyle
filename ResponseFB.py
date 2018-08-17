import sys
import random

sys.path.insert(0, "./NLG_Rap_Bot")
sys.path.insert(0, "./Artist_Rap_Bot")

from fbchat import log, Client
from fbchat.models import *

from Rap_NLG import Rap_NLG
from Rap_Artist import Rap_Artist






# Subclass fbchat.Client and override required methods
class NLGRapBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
        
        # If you're not the author, echo
        if author_id != self.uid:
            message = message_object.text
            print(message)
            response_list = Rap_NLG(message)
            response = ""
            for text in response_list:
                text = text[0].upper() + text[1:-1] #Capitilize first letter and remove last blank
                response = response + text + ". " #Add a period
				
            self.send(Message(text=response), thread_id=thread_id, thread_type=thread_type)

			
    def Listener(username, password):		
        client = NLGRapBot(username, password)
        client.listen()


	
	
	
	

# Subclass fbchat.Client and override required methods
class ArtistRapBot(Client):
	
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)
        
        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
        # If you're not the author, echo
        if author_id != self.uid:
            message = message_object.text
            print(message)
            response_list = Rap_Artist(message)
            response = ""
            for text in response_list:
                response = response + text + ". "
			
            self.send(Message(text=response), thread_id=thread_id, thread_type=thread_type)

			
    def Listener(username, password):
        client = ArtistRapBot(username, password)
        client.listen()
		
		
		

	