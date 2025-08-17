import anthropic
import ollama
from dotenv import load_dotenv
from openai import OpenAI
from IPython.display import Markdown, display, update_display
from scipy.optimize import anderson

load_dotenv()
system_prompt = """You are an assistant that is great in telling jokes"""
user_prompt = """Tell me a joke about how AI is overpowering humans"""

messages = [
    {
        "role": "system",
        "content": system_prompt
    },
    {
        "role": "user",
        "content": user_prompt
    }
]
MODEL = 'gpt-3.5-turbo' #'gpt-4o'
openai = OpenAI()
completion = openai.chat.completions.create(model=MODEL,messages=messages )
print(completion.choices[0].message.content)


claude = anthropic.Anthropic()
# Claude 3.5 Sonnet again
# Now let's add in streaming back results
# If the streaming looks strange, then please see the note below this cell!

result = claude.messages.stream(
    model="claude-3-5-sonnet-latest",
    max_tokens=200,
    temperature=0.7,
    system=[{"role": "system", "content": "You are an assistant that is great in telling jokes"}],
    messages=[
        {"role": "user", "content": user_prompt},
    ],
)

with result as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)



OLLAMA_MODEL = "llama3.2"




#response = ollama.chat(model=OLLAMA_MODEL, messages=messages)
#ollama.create(model=OLLAMA_MODEL, messages=messages)
#print(response['message']['content'])