# in-built camera fire detect

import numpy as np
import cv2

video = cv2.VideoCapture(0)

# 0,1,2,3 - camera connected to laptop
# we can also give file name as string it will read that file and do that process below

# video.set(cv2.CAP_PROP_FRAME_WIDTH , 1280)
# video.set(cv2.CAP_PROP_FRAME_HIEGHT , 720)
# setting width and height of the frame

while True:
    ret, frame = video.read()

    if not ret:
        print("Failed to read frame or video has ended")
        break

    frame = cv2.resize(frame, (900, 500))
    blur = cv2.GaussianBlur(frame, (15, 15), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # hsv values for large fire
    # lower = [18,50,50]
    # upper = [35,255,255]

    # hsv values with slight blue
    # lower = [10,0,204]
    # upper = [124,255,255]

    # hsv values with reddish orange thingy
    # lower = [20,0,230]
    # upper = [89,255,255]

    # Fire-related HSV values - tighter range to avoid false positives like pink paint
    lower = [5, 150, 150]  # Lower bound: more saturation and higher value
    upper = [20, 255, 255]  # Upper bound: higher saturation and value for fire colors

    lower = np.array(lower, dtype='uint8')
    upper = np.array(upper, dtype='uint8')

    mask = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(frame, hsv, mask=mask)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Ensure contours are found before proceeding
    if contours:
        max_countours = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(max_countours)
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(output, 'Fire', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    else:
        cv2.putText(output, 'No Fire Detected', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Fire Detection", output)

    if cv2.waitKey(100) & 0xFF == ord("q"): # pressing "q" will stop the camera
        break

cv2.destroyAllWindows()
video.release()
