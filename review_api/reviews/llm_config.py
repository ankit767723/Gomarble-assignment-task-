import os
from openai import OpenAI

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

def get_llm_client():
    return OpenAI(api_key=OPENAI_API_KEY)