import cv2
import os
import numpy as np

file = "../imgs/video/video1.mp4"
output_folder = "../imgs/video/frames"

os.makedirs(output_folder, exist_ok=True)

# Open video
cam = cv2.VideoCapture(file)
frame_count = 0

while True:
    ret, frame = cam.read()
    if not ret:
        break  # Exit loop when video ends

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
    cv2.imshow('frame', frame)
    frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
    cv2.imwrite(frame_filename, frame)
    frame_count += 1
    if cv2.waitKey(10) == ord('q'):
        break
# Release resources
cam.release()
print("Frame extraction completed!")
