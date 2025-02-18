import cv2
import numpy as np

file = "../imgs/video/video1.mp4"
cam = cv2.VideoCapture(file)

fps = int(cam.get(cv2.CAP_PROP_FPS))


while True:
    ret, frame = cam.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    canny = cv2.Canny(gray, 100, 200)

    lines = cv2.HoughLines(canny, 1, np.pi / 180, 200)

    if lines is not None:
        for rho, theta in lines[:, 0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 255), 2)
    cv2.imshow('Hough Lines', frame)
    if cv2.waitKey(10) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
