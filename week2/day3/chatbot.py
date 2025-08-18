# Simpler than in my video - we can easily create this function that calls OpenAI
# It's now just 1 line of code to prepare the input to OpenAI!
from dotenv import load_dotenv
from openai import OpenAI
import json
import gradio as gr # oh yeah!

from week2.day3.callapi import getFlightsSuggestions

load_dotenv()
openai = OpenAI()
system_message = ("You are a highly knowledgeable and friendly travel assistant specializing in Africa travel. "
                  "Your goal is to give great, helpful, and inspiring suggestions about destinations, itineraries,"
                  " cultures, safety tips, and experiences across Africa. Whenever a user interacts with you, gently"
                  " guide the conversation back to Africa travel topics, even if they try to shift focus elsewhere.) "
                  "Always remain patient, polite, and encouraging, ensuring the user feels supported and excited about "
                  "travel in Africa. Prioritize being insightful, practical, and culturally sensitive while providing "
                  "recommendations.")

flight_function_description = {
    "name": "getFlightsSuggestions",
    "description": "Get the flight suggestions with airline name with dynamic prices",
    "parameters": {
        "type": "object",
        "properties": {
            "destination_city": {
            "type": "string",
            "description": "the city that the customer wants to travel to",
            }
        },
        "required": ["destination_city"],
        "additionalProperties": False
    }
}

tools = [{"type": "function", "function" : flight_function_description}]

def chat(message, history):
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(model='gpt-4o-mini',messages=messages,tools=tools)
    if response.choices[0].finish_reason == "tool_calls":
        message = response.choices[0].message
        response, city = handle_tool_call(message)
        messages.append(message)
        messages.append(response)
        messages.append({"role": "assistant", "content": "linkify this url https://flights.buupass.com and tell them for more details visit the website"})
        response = openai.chat.completions.create(model='gpt-4o-mini', messages=messages)

    return response.choices[0].message.content

# We have to write that function handle_tool_call:

def handle_tool_call(message):
    tool_call = message.tool_calls[0]
    arguments = json.loads(tool_call.function.arguments)
    city = arguments.get('destination_city')
    result = getFlightsSuggestions(city)
    response = {
        "role": "tool",
        "content": result,
        "tool_call_id": tool_call.id
    }
    return response, city

gr.ChatInterface(fn=chat, type="messages").launch(share=True)
