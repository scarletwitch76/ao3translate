import requests
from bs4 import BeautifulSoup
import openai
import textwrap
from dotenv import load_dotenv
import os

load_dotenv()

# Set up the OpenAI API key
openai.api_key = os.getenv(key="OPENAI_API_KEY")

# Define the maximum number of tokens per translation request
MAX_TOKENS_PER_REQUEST = 5000

# Function to translate a given text using ChatGPT
def translate_text(text):
    # Divide the text into chunks that fit within the maximum number of tokens per request
    chunks = [text[i:i+MAX_TOKENS_PER_REQUEST] for i in range(0, len(text), MAX_TOKENS_PER_REQUEST)]
    
    # Initialize an empty list to store the translated chunks
    translated_chunks = []
    
    print('Total: '+str(len(chunks)))
    
    # Loop through the chunks and translate each one using ChatGPT
    for chunk in chunks:
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k-0613", max_tokens=MAX_TOKENS_PER_REQUEST, messages=[{"role": "user", "content": f'Translate the following text to English keeping format and blank lines:\n\n{chunk}\n\nTranslation:'}])
        # Extract the translated text from the response
        translated_chunk = response.choices[0].message.content
        translated_chunks.append(translated_chunk)
    
    return '\n'.join(translated_chunks)
            


# Function to translate a work from AO3
def translate_work(url):
    # Make an HTTP request to the AO3 website to get the HTML code of the work
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the text of the work within the HTML code
    work_text = soup.find('div', {'class': 'userstuff'}).text
    
    # Translate the text using ChatGPT
    return translate_text(work_text)
    


