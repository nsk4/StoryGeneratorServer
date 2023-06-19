import openai
import json

openai.api_key_path = "openai_api_key.txt"


def request_chat_completion(messages):
    print("messages:", messages)

    api_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=500,
                n=1,
                temperature=0.3
            )
    
    print("response:", api_response["choices"][0]["message"]["content"])
    return json.loads(api_response["choices"][0]["message"]["content"])

def generate_system_prompt():
    return 'Procedurally generate a short story with choices. Pick any theme you like. Keep story very short. The user can choose what to do in the next step of the story. Wait for user response. Generated text should be in the valid JSON format: {"text":"<main story text>", "options":["<list of options>"]}'
