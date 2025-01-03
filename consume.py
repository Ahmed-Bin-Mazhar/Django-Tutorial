import requests
print('testing')

response = requests.get('http://127.0.0.1:8000/drinks/4')
print(response.json())