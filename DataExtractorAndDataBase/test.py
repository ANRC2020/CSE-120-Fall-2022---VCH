import requests

register_URL = " http://127.0.0.1:5000/register"

parameters = {"username":"Dr. Abs","password":"awhbfkewabiw","firstname":"Abbas","lastname":"Siddiqui"}

response = requests.post(url=register_URL,params=parameters)
#if you could, create a json format, or text
# response.json()
print(response)

