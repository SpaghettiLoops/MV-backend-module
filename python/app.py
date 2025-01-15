from flask import Flask, request, jsonify
import json

# Load data from data.json
with open('data.json', 'r') as file:
    data = json.load(file)

app = Flask(__name__)

# POST - create a new snippet
@app.route('/snippets', methods=['POST'])
def create_snippet():
  try:
    new_snippet = request.get_json()
    if new_snippet.get('language') and new_snippet.get('code') and new_snippet.get('id'):
      data.append(new_snippet)
      return jsonify(data), 201
    else:
      return jsonify({'message': 'Parameters missing, please try again with a complete request'}), 404  
  except:
    return jsonify({'message': 'Invalid request'}), 400

# GET - GET all snippets
@app.route('/snippets', methods=['GET'])
def get_all_snippets():
  try:
    return jsonify(data)  
  except:
    return jsonify({'message': 'Invalid request'}), 400

# GET - get a snippet by id e.g snippets/4
@app.route('/snippets/<int:id>', methods=['GET'])
def get_snippet_by_id(id):
  try:
    snippet = next((snippet for snippet in data if snippet['id'] == id), None)
    if snippet:
      return jsonify(snippet)
    else:
      return jsonify({'message': 'Snippet not found'}), 404
  except:
    return jsonify({'message': 'Invalid request'}), 400

# GET get a snippet by language e.g. snippets/python
@app.route('/snippets/<language>', methods=['GET'])
def get_snippets_by_language(language):
  try:
    snippets = [snippet for snippet in data if snippet['language'].lower() == language.lower()]
    if snippets:
      return jsonify(snippets)
    else:
      return jsonify({'message': 'No snippets found for this language.'}), 404
  except:
    return jsonify({'message': 'Invalid request'}), 400
  
if __name__ == '__main__':
    app.run(debug=True, port=3000)
