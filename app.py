from flask import Flask, request, jsonify
from flask_cors import CORS
from story import Story

app = Flask(__name__)
CORS(app)

story = Story()


@app.route('/')
def index():
    return jsonify("Hi")


@app.route('/story')
def get_story():
    return jsonify(story.to_dict())

@app.route('/generate', methods=['GET', 'POST']) # TODO: remove GET
def generate_next_block():
    #selected_option = request.get_json()["option"]
    selected_option = request.args.get('option')

    if selected_option is None:
        app.logger.info("Starting a new story")
        #story = Story()
    else:
        app.logger.info("Received user response: " + selected_option)
        story.add_user_response(selected_option)
    story.generate_response()

if __name__ == '__main__':
    #app.run()

    a = str(story.to_dict())
    b = str(story.flatten_blocks())


    

    ret = get_story()
    print(ret)