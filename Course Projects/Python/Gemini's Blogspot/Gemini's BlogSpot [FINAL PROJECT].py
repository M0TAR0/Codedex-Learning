# This is a program created to be a blog generator, made following codedex guidelines, but using GEMINI.

#Import necessary libraries to use Gemini API
import os
from google import genai
from google.genai import types

#env package for API privacy
from dotenv import dotenv_values

config = dotenv_values(".env")

Gemini = genai.Client(api_key=config["API_KEY"]) #API KEY Reference (.env)

def generate_blog(paragraph_topic):
   blog_paragraph = Gemini.models.generate_content(
      model="gemini-2.5-flash",
      contents=["Write a paragraph about the following topic: " + paragraph_topic], #PROMPT
      config=types.GenerateContentConfig(
         temperature=0.3
      )
   ) 
   return blog_paragraph.text

keep_writing = True

#Loop to write until the user says otherwise
while keep_writing:
    answer = input("Write a paragraph? \"Y\" for yes, anything else for No: ")
    if answer == "Y":
        paragraph_topic = input("What would you like to write about? ")
        print("\n" + generate_blog(paragraph_topic) + "\n")
    else:
        keep_writing = False
      
#Made by: 
#Romel Ontiveros Mota 😇