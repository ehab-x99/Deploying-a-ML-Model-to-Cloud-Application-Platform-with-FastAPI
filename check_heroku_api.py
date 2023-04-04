# import requests

# # Define the data to be sent in the POST request
# data = {
#     "age": 32,
#     "workclass": "State-gov",
#     "education": "Some-college",
#     "maritalStatus": "Married-civ-spouse",
#     "occupation": "Exec-managerial",
#     "relationship": "Husband",
#     "race": "White",
#     "sex": "Female",
#     "hoursPerWeek": 40,
#     "nativeCountry": "United-States"
# }

# # Make a POST request to the API endpoint and store the response
# response = requests.post('https://project3-app.herokuapp.com/', json=data)

# # Check the response status code and raise an error if it's not 200
# if response.status_code != 200:
#     print("Error: Received status code %d" % response.status_code)
#     print("Response body: %s" % response.text)
#     exit(1)

# # Try to decode the response body as JSON and handle any errors
# try:
#     response_json = response.json()
#     print(response_json)
# except ValueError as e:
#     print("Error decoding response body as JSON: %s" % e)
#     print("Response body: %s" % response.text)
#     exit(1)

# # Print the response status code and body
# print("Response code: %s" % response.status_code)
# print("Response body: %s" % response_json)

import requests


df = {
    "age": 32,
    "workclass": "State-gov",
    "education": "Some-college",
    "maritalStatus": "Married-civ-spouse",
    "occupation": "Exec-managerial",
    "relationship": "Husband",
    "race": "White",
    "sex": "Female",
    "hoursPerWeek": 40,
    "nativeCountry": "United-States"
    }
url='https://project3-app.herokuapp.com'
r = requests.post(url, json=df)

# assert r.status_code == 200
# print(r.json())
# r_data = r.json()
# print(r_data['prediction'])
print("%s",r.status_code)
print("%s", r.content)
# print("Response code: %s" % r.status_code)
# print("Response body: %s" % r.json())
