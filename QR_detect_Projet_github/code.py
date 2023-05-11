from PyKakao import Message
api = Message(service_key = "REST API키 입력")
auth_url = api.get_url_for_generating_code()

print(auth_url)