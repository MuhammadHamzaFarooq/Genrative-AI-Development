import requests
from requests.models import Response
from requests.structures import  CaseInsensitiveDict

response : Response = requests.get("https://simple-books-api.glitch.me/status")
print("api response: ", response)

# get status for this response object
status_code : int = response.status_code
print("status code: ", status_code)

# get json response object
json_response : dict = response.json()
print("json response: ", json_response,type(json_response))

# get response text
response_txt : str = response.text
print("response text: ", response_txt, type(response_txt))

# get response headers
response_headers : CaseInsensitiveDict = response.headers
print("response headers: ", response_headers, type(response_headers))

# print all of responses like status code, json, text, headers
print(response.status_code, response.json(), response.text, response.headers)