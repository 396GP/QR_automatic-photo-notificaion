import cv2

import cv2

# 웹캠에서 영상을 읽어옵니다.
cap = cv2.VideoCapture(0)

while True:
    # 영상을 프레임 단위로 읽어옵니다.
    ret, frame = cap.read()

    # 프레임이 제대로 읽어졌는지 확인합니다.
    if not ret:
        break

    # 프레임을 출력합니다.
    cv2.imshow('frame', frame)

    # 'q' 키를 누르면 종료합니다.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 사용한 자원을 해제합니다.
cap.release()
cv2.destroyAllWindows()
