import cv2
import controller as cnt
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.8, maxHands=2)

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    frame = cv2.flip(frame, 1)
    hands, img = detector.findHands(frame)

    if hands:
        lmList = hands[0]
        fingerUp = detector.fingersUp(lmList)

        print(fingerUp)
        cnt.led(fingerUp)

        # Mostrar el número de dedos levantados
        numFingers = fingerUp.count(1)
        cv2.putText(frame, f'Dedos Levantados: {numFingers}', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == ord("k"):
        break

video.release()
cv2.destroyAllWindows()
