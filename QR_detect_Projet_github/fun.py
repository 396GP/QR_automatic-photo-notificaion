from PyKakao import Message
import json
import csv

# 파일에서 access_token 불러오기
with open('kakao_code.json', 'r') as f:
    tokens = json.load(f)

# access_token으로 메시지 보내기
api = Message(service_key="RESTAPI 키 입력")
api.set_access_token(tokens['access_token'])

# csv 파일에서 정보 읽어오기
with open('qr_code_result.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = list(csv_reader)
    number = rows[0][0]  # 1행 1열의 정보
    data = rows[2][0]  # 3행 1열의 정보

text = f"({number}){data}가 배송되었습니다."
link = {
        "web_url": "https://developers.kakao.com",
        "mobile_web_url": "https://developers.kakao.com"
    }
button_title = "바로 확인"
api.send_text(text=text, link={}, button_title=button_title)

content = {
            "title": "택배 도착 알림",
            "description": f"http://본인 IP/qr_code_result",
            "image_url": "http://본인 IP/qr_code_result",
            "image_width": 640,
            "image_height": 640,
            "link": {
                "web_url": "http://www.daum.net",
                "mobile_web_url": "http://m.daum.net",
                "android_execution_params": "contentId=100",
                "ios_execution_params": "contentId=100"
            }
        }

api.send_feed(content=content)