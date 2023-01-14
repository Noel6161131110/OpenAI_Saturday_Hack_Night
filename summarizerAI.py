import os
import openai

#openai.api_key = os.getenv('API_KEY') #Setting GPT-3 API-KEY (text-davinci-002)

openai.api_key_path = 'apikey.txt'

warning = "Size too small....."

def response_Summary(document_Text,user_choice = "Neutral"):

    if user_choice == "Neutral":
        max_words = 80
        temp_set = 0.2
    elif user_choice == "Defined":
        max_words = 50
        temp_set = 0.5
    elif user_choice == "Creative":
        max_words = 220
        temp_set = 0.8


    if len(document_Text) > 100:
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt="Please summarize this article for me in a few sentences: "+ document_Text,
            temperature= temp_set,
            max_tokens= max_words,
        
        )
        return response["choices"][0]["text"]

    return warning

    
 

