#!/usr/bin/env python
# coding: utf-8

# In[3]:


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# isso aqui só precisa para corrigir o bug
from spacy.cli import download

download("en_core_web_sm")

class ENGSM:
    ISO_639_1 = 'en_core_web_sm'
    


# In[9]:


chatbot = ChatBot("teste", tagger_language=ENGSM)

conversa = [
    "oi",
    "olá, tudo bem?",
    "tudo certo",
    "que bom, como posso te ajudar?"
]

trainer = ListTrainer(chatbot)
trainer.train(conversa)


# In[1]:


while True:
    mensagem = input("Mande uma mensagem para o chatbot:")
    if mensagem == "parar":
        break
    resposta = chatbot.get_response(mensagem) 
    print(resposta)


# In[8]:


chatbot.storage.drop()


# In[ ]:




