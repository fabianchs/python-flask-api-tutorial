from flask import Flask, jsonify, request
import json
#from flask import jsonify
app = Flask(__name__)

todos= [{ "label": "My first task", "done": False }]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text= jsonify(todos) #flask.
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    json_text= jsonify(todos)

    print("Incoming request with the following body", request_body)
    return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    if position<len(todos):
        todos.pop(position)
    else:
        return 'error, that task does not exists'
    json_text= jsonify(todos)
    return 'OK, task deleted'

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)