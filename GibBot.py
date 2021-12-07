import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  engine="davinci-instruct-beta-v3",
  prompt=" You are talkin to Gib , is a chat bot that provides with information about you location , like hotels,  monuments and restaurants\n\nPreson:Hellow Gib\nGib:Hi, how can i help you today?\n\nPreson: I was loking for somthing to do in the city like visiting a monument\nGib:Perft, near you are two famous monuments that you can visit, one is the Eiffel Tower and the other the  Field of Mars\n\nPreson: Perfect , can you recommend me some vegan restaurant near by?\nGib:In the next intersection you have a nice restaurna with five start reviews\n\nPerson: Can you recomend me any hotel?\nGib: You have one hotel that is local to the area with eco firndly politics and vegan bufet\n\nPerson: Can you recomend me some more activities?\nGib: You can go to the lake and  ride a boat\n\nPerson: Can you point me to the neares train station?\nGib:Yes, it is just two blocks from here\n\nPerson:Can you recomend me a restauran to eat?\nGib: There is a vegan restauran near by with a five start rating,/n  temperature=0.7,",
  max_tokens=96,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.19
)

from dotenv import load_dotenv
from random import choice
from flask import Flask, request
import os
import openai
load_dotenv()
openai.api_key = os.getenv('key')
completion = openai.Completion()
start_sequence = "\nGib:"
restart_sequence = "\n\nPerson:"
session_prompt = 'You are talkin to Gib , is a chat bot that provides with information about you location , like hotels,  monuments and restaurants\nPreson:Hellow Gib\nGib:Hi, how can i help you today?\nPreson: I was loking for somthing to do in the city like visiting a monument\nGib:Perft, near you are two famous monuments that you can visit, one is the Eiffel Tower and the other the  Field of Mars\nPreson: Perfect , can you recommend me some vegan restaurant near by?\nGib:In the next intersection you have a nice restaurna with five start reviews\nPerson: Can you recomend me any hotel?\nGib: You have one hotel that is local to the area with eco firndly politics and vegan bufet\nPerson: Can you recomend me some more activities?\nGib: You can go to the lake and  ride a boat\nPerson: Can you point me to the neares train station?\nGib:Yes, it is just two blocks from here\nPerson:Can you recomend me a restauran to eat?\nGib: There is a vegan restauran near by with a five start rating'

def ask(question, chat_log=None):
 response = openai.Completion.create(
 engine="davinci",
 temperature=0.8,
 max_tokens=150,
 top_p=1,
 frequency_penalty=0,
 presence_penalty=0.3,
 stop=['\n'],
 )
 prompt_text = f"{chat_log}{restart_sequence}:{question}{start_sequence}:"
 
 def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:' 
    response = openai.Completion.create(
    engine="davinci",
    prompt=prompt_text,
    temperature=0.8,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.3,
    stop=['\n'],
 )
 story = response["choices"][0]["text"]
 
 def ask(question, chat_log=None):
     prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
     response = openai.Completion.create(
     engine="davinci",
     prompt=prompt_text,
     temperature=0.8,
     max_tokens=150,
     top_p=1,
     frequency_penalty=0,
     presence_penalty=0.3,
     stop=["\n"],
     )
 story = response['choices'][0]['text']
 return str(story)
def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None: chat_log = session_prompt 
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'