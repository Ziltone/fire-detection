from ultralytics import YOLO
import cv2

# downlaoded the Ml model named "best.pt".
# dataset used from roboflow, can also ur own model.

model = YOLO("best.pt")  # if not working try with the entire path

cap = cv2.VideoCapture(0)
# source - cameras(0,1,2,3...) or use video files too.
# save - True -> if wanted to save the results.

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(source=frame, imgsz=640, conf=0.6, save=False, show=True)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
