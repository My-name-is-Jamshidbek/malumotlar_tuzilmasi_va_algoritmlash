import cv2
import numpy as np

cap = cv2.VideoCapture('Sharipov.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
previous_positions = {}
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    current_positions = {}
    for i, contour in enumerate(contours):
        if cv2.contourArea(contour) > 500:
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                current_positions[i] = (cx, cy)
                if i in previous_positions:
                    prev_cx, prev_cy = previous_positions[i]
                    movement_distance = np.sqrt((cx - prev_cx) ** 2 + (cy - prev_cy) ** 2)
                    if movement_distance > 10:
                        cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
                    else:
                        cv2.circle(frame, (cx, cy), 5, (128, 128, 255), -1)
    previous_positions = current_positions
    cv2.imshow('Detected Movement', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
