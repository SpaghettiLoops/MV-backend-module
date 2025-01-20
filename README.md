# How to pull:

git fetch 
git pull

# How to push:

git add .
git commit -m "message here"
git push -u origin main 

# How to run it

## PYTHON

python3 youfile.py

## JAVA

open in intelliJ
cd to the correct place

1. In the terminal type:  ./gradlew bootRun
2. Then go to postman and type:
 - GET http://localhost:8080/snippets
 - GET http://localhost:8080/snippets/1
 - GET http://localhost:8080/snippets?lang=Python

This will check each endpoint is working.

## Javascript

open in VSCode or intelliJ
cd to the correct place

1. npm install express
2. npm install
3. node app.js
4. Then go to http://localhost:3000 and type:
- http://localhost:3000/snippets
- http://localhost:3000/snippets/:id
- http://localhost:3000/snippets/language/python

# PYTHON BCRYPT EXAMPLE

import bcrypt

password = "password123"  # example password

password_bytes = password.encode("utf-8")  # convert password to bytes

salt = bcrypt.gensalt()  # generate a salt

hashed_password = bcrypt.hashpw(password_bytes, salt)  # hash the password

print("Hashed password:", hashed_password)  # output the hashed password with salt

# To verify the password later
password_check = "password123"  # example password to verify
password_check_bytes = password_check.encode("utf-8")

# Check if the entered password matches the hashed password
if bcrypt.checkpw(password_check_bytes, hashed_password):
    print("Password match!")
else:
    print("Password does not match.")
