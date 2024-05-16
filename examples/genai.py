# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv, find_dotenv
import google.generativeai as genai

load_dotenv(find_dotenv(), override=True)

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY, transport="rest")


version = 'models/gemini-1.5-flash-latest' # @param ["models/gemini-1.5-flash-latest", "models/gemini-1.5-pro-latest", "models/gemini-1.0-pro-latest"]
model = genai.GenerativeModel(version)

model_info = genai.get_model(version)
print(f'{version} - input limit: {model_info.input_token_limit}, output limit: {model_info.output_token_limit}')
