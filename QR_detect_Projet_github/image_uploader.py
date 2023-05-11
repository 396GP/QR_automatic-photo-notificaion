from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'QR 코드 결과 이미지: <a href="/qr_code_result">{}</a>'.format(file_path)

@app.route('/qr_code_result')
def qr_code_result():
    return send_from_directory(upload_dir, 'qr_code_result.jpg')

if __name__ == '__main__':
    # qr_code_result.jpg 파일의 경로
    file_path = 'qr_code_result.jpg'

    # 이미지 파일을 업로드할 서버 경로
    upload_dir = './'

    # qr_code_result.jpg 파일을 업로드할 서버 경로에 복사
    if os.path.exists(file_path):
        new_file_path = os.path.join(upload_dir, 'qr_code_result.jpg')
        os.system(f'cp {file_path} {new_file_path}')

    app.run(host='0.0.0.0', port=80)
