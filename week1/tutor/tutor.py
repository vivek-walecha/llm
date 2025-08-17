import os
from idlelib.rpc import response_queue

import requests
import json
from typing import List
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from selenium import webdriver
from IPython.display import Markdown, display, update_display
from openai import OpenAI
import webbrowser
from pathlib import Path

MODEL_GPT = 'gpt-4o-mini'
MODEL_LLAMA = 'llama3.2'
load_dotenv()
openai = OpenAI()
my_question = input("Please enter your question:")
question = """Please tell me about this code more : override fun onCreateViewHolder(viewGroup: ViewGroup, viewType: Int): ViewHolder {
        val view = LayoutInflater.from(viewGroup.context)
                .inflate(R.layout.text_row_item, viewGroup, false)

        return ViewHolder(view)
    }"""

system_prompt = "You are a helpful technical tutor who answers questions about android sdk, python, software engineering, data science and LLMs"
user_prompt = "Please give a detaaild explanation to the following question:" + my_question

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt},
]

response = openai.chat.completions.create(model=MODEL_GPT, messages=messages)
result = response.choices[0].message.content
print(result)


