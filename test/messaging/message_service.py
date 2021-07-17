'''
Created on 17 Jul 2021

@author: eytan
'''

from nameko.rpc import rpc

messages = {}


class MessageService:
    name = "messaging_service"
    
    @rpc
    def send(self, sender, receipient, message):
        if receipient not in messages:
            messages[receipient] = []
        messages[receipient].append((sender, message))
        
    @rpc
    def receive(self, recipient):
        result = messages.get(recipient, [])
        messages[recipient] = []
        return result
