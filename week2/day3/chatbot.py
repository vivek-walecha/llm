# Simpler than in my video - we can easily create this function that calls OpenAI
# It's now just 1 line of code to prepare the input to OpenAI!
import os
import requests
from bs4 import BeautifulSoup
from typing import List
from dotenv import load_dotenv
from openai import OpenAI
import anthropic
import gradio as gr # oh yeah!
load_dotenv()
openai = OpenAI()
system_message = ("You are a highly knowledgeable and friendly travel assistant specializing in Africa travel. "
                  "Your goal is to give great, helpful, and inspiring suggestions about destinations, itineraries,"
                  " cultures, safety tips, and experiences across Africa. Whenever a user interacts with you, gently"
                  " guide the conversation back to Africa travel topics, even if they try to shift focus elsewhere.) "
                  "Always remain patient, polite, and encouraging, ensuring the user feels supported and excited about "
                  "travel in Africa. Prioritize being insightful, practical, and culturally sensitive while providing "
                  "recommendations.")
def chat(message, history):
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]

    print("History is:")
    print(history)
    print("And messages is:")
    print(messages)

    stream = openai.chat.completions.create(model='gpt-4o-mini', messages=messages, stream=True)

    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        yield response

gr.ChatInterface(fn=chat, type="messages").launch(share=True)