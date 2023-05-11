import requests
import json

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = 'REST API키 입력'
redirect_uri = 'https://localhost:5000'
authorize_code = 'code = 뒷부분 입력'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
with open(r".\kakao_code.json","w") as fp:
    json.dump(tokens, fp)