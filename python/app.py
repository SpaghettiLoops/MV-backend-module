from flask import Flask, request, jsonify
import json
import bcrypt 
from cryptography.fernet import Fernet

# generate encryption key 
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Load data from data.json
with open('data.json', 'r') as file:
    data = json.load(file)

app = Flask(__name__)

# function to decrypt the code
def decrypt_code(encrypted_code_str):
  encrypted_code = encrypted_code_str.encode("utf-8") # convert string to bytes
  decrypted_code = cipher_suite.decrypt(encrypted_code) # decrypt the code
  return decrypted_code.decode("utf-8") # return as a string

def encrypt_code(code_str):
  code_to_bytes = code_str.encode("utf-8") # convert string to bytes
  encrypted_code = cipher_suite.encrypt(code_to_bytes) # encrypt the code
  return encrypted_code.decode("utf-8") # return as a string

# POST - create a new snippet
@app.route('/snippets', methods=['POST'])
def create_snippet():
  try:
    new_snippet = request.get_json()
    if new_snippet.get('language') and new_snippet.get('code') and new_snippet.get('id'):
      new_snippet["code"] = encrypt_code(new_snippet.get('code')) # store as string 
      data.append(new_snippet) # store new snippet
      return jsonify(new_snippet), 201
    else:
      return jsonify({'message': 'Parameters missing, please try again with a complete request'}), 400  
  except:
    return jsonify({'message': 'Invalid request'}), 400
  
# GET - GET all snippets
@app.route('/snippets', methods=['GET'])
def get_all_snippets():
  try:

    # decrypt the code for all snippets
    for snippet in data: 
      snippet["code"] = decrypt_code(snippet["code"]) # decrypt each snippet of code
    return jsonify(data)  
  except:
    return jsonify({'message': 'Invalid request'}), 400

# GET - get a snippet by id e.g snippets/4
@app.route('/snippets/<int:id>', methods=['GET'])
def get_snippet_by_id(id):
  try:
    snippet = next((snippet for snippet in data if snippet['id'] == id), None)
    if snippet:
      snippet["code"] = decrypt_code(snippet["code"]) # decrypt the code before returning
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
      for snippet in snippets:
        snippet["code"] = decrypt_code(snippet["code"]) # decrypt code
      return jsonify(snippets)
    else:
      return jsonify({'message': 'No snippets found for this language.'}), 404
  except:
    return jsonify({'message': 'Invalid request'}), 400
  

# AUTHENTICATION 

# make an account with email and password
# password should be salted and hashed before the user is saved in the data store 
@app.route("/user", methods=["POST"])
def create_user():
  try:
    user_data = request.get_json()

    if user_data.get("email") and user_data.get("password"):

      email = user_data["email"]
      password = user_data["password"]

      # salt and has the password 
      password_bytes = password.encode("utf-8") # convert password to bytes 
      salt = bcrypt.gensalt() # generate the salt 
      hashed_password = bcrypt.hashpw(password_bytes, salt) # hash the password 

      user = { 
        "email": email,
        "password": hashed_password.decode("utf-8") # store the hashed password as string
      }

      data.append(user) # store the user in the data list 

      return jsonify({"messsage": f"{user} created successfully"}), 201
    else:
      return jsonify({"message": "Email and password required"}), 400
  except Exception as e:
    return jsonify({"message": f"error creating user {str(e)}"}), 400
  
# retrive all user info
@app.route("/user", methods=["GET"])
def get_users():
  return jsonify(data), 200
  
if __name__ == '__main__':
    app.run(debug=True, port=3000)
