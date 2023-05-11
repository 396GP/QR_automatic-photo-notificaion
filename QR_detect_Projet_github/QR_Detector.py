import cv2
import numpy as np
from pyzbar.pyzbar import decode
import csv
import os

# 이미지 불러오기
img = cv2.imread('qr_code3.jpg')

# QR 코드 인식
decoded_objs = decode(img)

# 인식 결과가 있을 때까지 이미지를 회전시키며 QR 코드 인식 시도
while not decoded_objs:
    # 이미지 회전 각도
    angle = 0

    # 이미지 회전 중심점
    center = tuple(np.array(img.shape[1::-1]) / 2)

    # 회전 변환 행렬 계산
    M = cv2.getRotationMatrix2D(center, angle, 1)

    # 이미지 회전
    img = cv2.warpAffine(img, M, img.shape[1::-1], flags=cv2.INTER_LINEAR)

    # QR 코드 인식
    decoded_objs = decode(img)

    # 인식이 안 됐을 때 이미지 출력
    if not decoded_objs:
        cv2.imshow('Processed Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print('QR 코드 인식 실패')
        exit(0)

# 인식된 QR 코드 위치에 대해 빨간색 박스 그리기
for obj in decoded_objs:
    # QR 코드 위치 추출
    bbox = obj.rect

    # 빨간색 박스 그리기
    cv2.rectangle(img, (bbox.left, bbox.top), (bbox.left + bbox.width, bbox.top + bbox.height), (0, 0, 255), 2)

    # QR 코드 정보 가져오기
    data = obj.data.decode("utf-8")
    print("QR 코드 정보:", data)

    # 이미지 저장
    cv2.imwrite('qr_code_result.jpg', img)

    # CSV 파일에 정보 저장
    with open('qr_code_result.csv', mode='w', newline='') as csv_file:
        fieldnames = ['QR 코드 정보']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # 쉼표로 구분된 정보를 CSV 파일에 입력
        info_list = data.split(',')
        for i, info in enumerate(info_list):
            writer.writerow({'QR 코드 정보': info.strip()})

# qr_code_result.csv에서 정보 읽어오기
with open('qr_code_result.csv', mode='r') as qr_file:
    qr_reader = csv.reader(qr_file)
    qr_info = [row[0] for i, row in enumerate(qr_reader) if 3 <= i <= 6]

# base_info.csv에서 정보 읽어오기
with open('base_info.csv', mode='r') as base_file:
    base_reader = csv.reader(base_file)
    base_info = [row[0] for i, row in enumerate(base_reader) if 0 <= i <= 3]

# 일치하는 정보 찾기
for i, qr_code in enumerate(qr_info):
    if qr_code in base_info:
        # 일치하는 정보가 있을 때 fun.py 실행
        os.system('python fun.py')
        os.system('python image_uploader.py')
        break
else:
    print('QR 코드 정보와 기준 정보가 일치하지 않습니다.')

# 결과 이미지 창에 표시
cv2.imshow('Processed Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


