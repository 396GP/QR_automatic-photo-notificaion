1. kakao developer에 가입 및 내 애플리케이션에서 애플리케이션 추가
2. REST API키 확인
3. 허용  IP 주소에 본인 IP/CIDR 추가, 카카오 로그인에 Ridirect URL http://localhost:5000을 추가
3. code.py를 열기 후
4. REST API키 입력
5. 실행 및 터미널에 나오는 링크에 접속
6. 카카오톡 아이디와 비밀번호를 입력
7. https://localhost:5000/?code= 뒷부분을 복사
8. gogo.py 열기 및 rest_api_key에 rest api, authorize_code에 7에서 복사한 키 입력
9. gogo.py 실행
10. QR_Detector.py 실행
11. 카톡에서 사진이 안보이면 본인 IP를 포트포워딩해서 외부에서 접속가능하게 해야함