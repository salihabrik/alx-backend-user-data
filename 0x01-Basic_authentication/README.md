# Flask Basic Authentication Project

This Flask project implements basic authentication for an API using Flask's framework. It includes features for handling unauthorized and forbidden access, a custom authentication class (BasicAuth), and supports Basic Authentication.

Getting Started
Prerequisites
Python 3.x
Flask
Installation
Clone the repository:

```
git clone https://github.com/yourusername/flask-basic-authentication.git
cd flask-basic-authentica
```
Install dependencies:

```
pip install -r requirements.txt
```
Usage
Set the environment variable for authentication type:

```
export AUTH_TYPE=basic
```
Run the Flask application:

```
python api/v1/app.py

```
Access the API endpoints and test basic authentication.

Project Structure
api/v1/app.py: Main Flask application file.
auth.py: Contains the Auth and BasicAuth classes for authentication.
tests/: Directory for test cases.
Tasks and Features
The project includes the following tasks and features:

Task 0: Handling Unauthorized Access (401)
Task 1: Handling Forbidden Access (403)
Task 3: Authentication Class (Auth)
Task 4: Defining Unauthenticated Routes
Task 5: Request Verification
Task 6: Basic Authentication Implementation
Task 7: Extracting Base64 from Basic
Task 8: Decoding Base64
Task 9: Extracting User Credentials
Task 10: User Object Creation
Task 11: Updating current_user method
Contributing
Feel free to contribute to the project by opening issues or submitting pull requests. Your feedback and contributions are welcome!

License
This project is licensed under the MIT License.