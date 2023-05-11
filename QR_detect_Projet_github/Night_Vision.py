import cv2

# 이미지 불러오기
img = cv2.imread('night_image_3.jpg')

# 밝기 조정
brightened_img = cv2.add(img, 50)

# 그레이스케일 이미지로 변환
gray_img = cv2.cvtColor(brightened_img, cv2.COLOR_BGR2GRAY)

# 대비 조정
equalized_img = cv2.equalizeHist(gray_img)

# 결과 이미지 저장
cv2.imwrite('processed_image.png', equalized_img)

# 결과 이미지 창에 표시
cv2.imshow('Processed Image', equalized_img)
cv2.imshow('original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()