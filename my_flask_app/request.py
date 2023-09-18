import requests

url = 'http://127.0.0.1:5000/results'

r = requests.post(url, json = {'tv': 250,'radio': 230,'newspaper': 211})
print('Code Working!!!')
# url1='http://127.0.0.1:5000/'


# print(requests.get(url1))
print(r.json)


