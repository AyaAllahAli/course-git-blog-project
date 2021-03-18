#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 12:54:32 2021

@author: ayaali
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 10:43:02 2021

@author: ayaali
"""
import io
import json
import sys

from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_EN


with open('/Users/ayaali/Documents/Geni_chatbot/Genei/question_new.txt') as fl:
    mylist = [line.rstrip('\n') for line in fl]
    
    questions=["Has DeNovoSeq a job tracking system? ","What is functional annotation? ", "Which assembler should I use if I manage prokaryotic data?",
               "What is the FTP browser of DeNovoSeq?"];

default_engine = SnipsNLUEngine()
#%%

engine = SnipsNLUEngine(config=CONFIG_EN)
with io.open("/Users/ayaali/Documents/Geni_chatbot/Genei/dataset.json") as fil:
    dataset = json.load(fil)

#%%
res = []
with open('/Users/ayaali/Documents/Geni_chatbot/Genei/out_new.txt', 'w') as f:
    engine.fit(dataset)
    seed = 42
    engine = SnipsNLUEngine(config=CONFIG_EN, random_state=seed)
    engine.fit(dataset)
    for ques in mylist:
        parsing = engine.parse(ques)
        #print(json.dumps(parsng, indent=2))
        res.append(parsing)
    f.write(json.dumps(res, indent=2))
f.close()


#%%
# with io.open("/Users/ayaali/Documents/Geni_chatbot/Genei/out.txt") as fil:
#     res = json.load(fil) 

# res 

Dicjason={}
for r in range(0,len(res)):
    
   intentName = res[r]['intent']['intentName']
   if not intentName in Dicjason:
       Dicnested={}
       Dicjason[intentName] = Dicnested ;
   slots = res[r]['slots']
   if len(slots) ==0 :
       Dicjason[intentName] = ""
   else:    
       entityName=res[r]['slots'][0]['rawValue']
       Dicnested = Dicjason[intentName]
       
       Dicnested [entityName]=""
#with open('/Users/ayaali/Documents/Geni_chatbot/Genei/out_test.txt', 'w') as f:       
with open('/Users/ayaali/Documents/Geni_chatbot/Genei/out_jason.json', 'w') as f:
    f.write(json.dumps(Dicjason, indent=2))
    f.close()

# intents = engine.get_intents("Hey, lthe variantseq how it works? ")
# print(json.dumps(intents, indent=2))
# engine_bytes = engine.to_byte_array()
# loaded_engine = SnipsNLUEngine.from_byte_array(engine_bytes

#%%
import difflib

print("Hi I am Genei your virtual assistant How can I help you\n")
while True:
    moresring=""
    ques=input(f"PLEASE ENTER YOR QUESTION  {moresring}\n")
    if(ques!="" or ques!= "no" or ques=="No"):
        parsing = engine.parse(ques)
        intent = parsing["intent"]["intentName"]
        slots = parsing['slots']
        if len(slots) !=0 :
            Key_value=parsing["slots"][0]["rawValue"]
            
        else:
            Key_value=intent
           
        with open('/Users/ayaali/Documents/Geni_chatbot/Genei/out_jason.json') as json_file:
        #json_file="/Users/ayaali/Documents/Geni_chatbot/Genei/out_jason.json"
              data=json.load(json_file)
              answer=data[intent]
              if(Key_value in answer):
                  if(len(slots)!=0):
                     
                      an=answer[Key_value]
                      print(f'\n{an}')
                  else:
                      answer=data[intent]
                      print(f'\n{answer}')
              else:
                 word_match=difflib.get_close_matches(Key_value,answer)
                 response=input(f"I am sorry i don't understand what do you mean with the word {Key_value}\n do you mean tthese {word_match} \n")
                 if(response=="yes" or response=="YES" or response=="Yes"):
                         Key_value=word_match[0]
                         if(len(slots)!=0):
                         
                              an=answer[Key_value]
                              print(f'\n{an}')
                         else:
                               answer=data[intent]
                               print(f'\n{answer}')
                 else:
                     respon=input("OK, will you please write your question again")
        
    else:
       print("OK, it was a pleasure to help you  Good by ")
       break  
    moresring="If you have another one"              
#%%