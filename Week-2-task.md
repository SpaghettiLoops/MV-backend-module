User Stories:
Encryption
    As a user, I want all snippets to be encrypted before being saved into the database, so that I feel confident my code can’t be stolen if the database is compromised
    As a user, I want the snippet to be decrypted before it is returned from the API, so that I can actually read it
Authentication
    As a user, I want to make an account with my email and password, so that I can have an identity on Snippr.io

Functional Requirements:
Encryption
    When a POST request is made to /snippet, the code content of the body should be encrypted before saving in the datastore
    When a GET request is made to /snippet (or any subroute), the code content should be decrypted before returning
Authentication
    When a POST request is made to /user with email and password in the body, the password should be salted and hashed before the user is saved in the data store.
    Bonus: When a GET request is made to /user, only the user whose correct credentials are provided should be returned. The response must not contain the password (or a hash of the password). This is therefore a protected endpoint and can only be accessed if email and password are provided with the request.

Non-Functional Requirements
    Continue in the same project repo you started last week, using the stack which aligns with the language used in your workplace.
    Refer to official documentation for help with encryption and hashing libraries (most languages have support for this, either directly or through packages). See below for guidance.
    Any secret keys should be saved as environment variables, not hard-coded into the application code.