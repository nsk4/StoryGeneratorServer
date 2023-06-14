import openai
import json

openai.api_key_path = "openai_api_key.txt"


def request_chat_completion(messages):
    api_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=500,
                n=1
            )
    #return api_response["choices"][0]["message"]

    return json.loads(api_response["choices"][0]["message"]["content"])

def generate_system_prompt():
    #return "Procedurally generate a short story with choices. Generated text should consist of the main text and listed options. The user can choose what to do in the next step of the story. Format the response into a json format like: {'text':'<main story text>', 'options':[<list of options>]}."
    return 'Procedurally generate a short story with choices. The user can choose what to do in the next step of the story. Wait for user response. Keep story very short. Pick any theme you like. Generated text should be in the JSON format: {"text":"<main story text>", "options":[<list of options>]}.'
