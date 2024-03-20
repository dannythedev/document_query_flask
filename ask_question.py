import requests

# Written by Daniel Stempo.

# The URL of the REST API endpoint. This should point to the Flask application running on localhost.
api_url = 'http://localhost:5000/ask'

# Prompt the user to type a question.
print("Type a question you'd like to ask.\nQ:")
# Read the user's question from the command line.
question = input()

# Prepare the data payload for the POST request, which includes the question.
data = {'question': question}

try:
    response = requests.post(api_url, json=data)
    if response.status_code == 200:
        answer = response.json().get('answer', 'No answer provided')
        print(f"A: {answer}")
    else:
        print(f"Failed to get an answer. Reason: {response.text} Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred while making the request: {e}")
