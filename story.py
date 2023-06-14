import openai_api
from story_block import StoryBlock
#import json

class Story:
    def __init__(self):
        self.story_blocks = []
        self.story_blocks.append(StoryBlock("system", openai_api.generate_system_prompt(), []));

    def add_user_response(self, response):
        self.story_blocks.append(StoryBlock("user", response, []))

    def add_assistant_response(self, response):
        self.story_blocks.append(StoryBlock("assistant", response["text"], response["options"]))
        
    def generate_response(self):
        blocks = []
        for block in self.story_blocks:
            if block.options == []:
                content = block.text
            else:
                content = str({"text": block.text, "options": block.options})
            blocks.append({"role": block.role, "content": content})

        response = openai_api.request_chat_completion(blocks)
        self.add_assistant_response(response)

    def to_dict(self):
        blocks = []
        for block in self.story_blocks:
            blocks.append({"role": block.role, "content": {"text": block.text, "options": block.options}})
        return blocks
    
if __name__ == '__main__':
    a = Story()
    a.generate_response()
    #a.add_user_response("Option 2")
    #a.generate_response();
    print(a.get_story_blocks())
