import os
import openai
import time

api_key_1 = "<insert your API key here>"

# Set the API key
openai.api_key = api_key_1 

prompt = input("start: ")
while True:
    # Have the first model respond to the prompt
    response_1 = openai.Completion.create(engine="text-davinci-002", prompt=prompt,max_tokens=50)
    response = response_1["choices"][0]["text"].replace("\n", "")
    print(f"Model 1: "+response+"\n")
    
    time.sleep(2)
    
    # Have the second model respond to the prompt
    response_2 = openai.Completion.create(engine="text-curie-001", prompt=response,max_tokens=50)
    new_response = response_2["choices"][0]["text"].replace("\n", "")
    print(f"Model 2: "+new_response+"\n")
    prompt=new_response
