# 🔥 Fire Detection System
A real-time fire detection system using both classical image processing **(HSV color filtering)** and a **YOLOv8** deep learning model using dataset from **Roboflow**. This project showcases how different methods can be applied for early fire identification, helping improve safety, awareness, and reaction time during emergencies.


📂 Features

* Real-time fire detection using HSV color segmentation.

* AI-based detection using YOLOv8 and a custom best.pt model.

* Ability to test with live camera input or a video file.

* Visual alerts when fire is detected.

* HSE (Health, Safety, and Environment) diagram/image added for better understanding of safety zones and context.

* A utility script `test_camera.py` to verify if the camera is working correctly.

📸 Project Files
* `fire_detect_hse.py` — HSV-based fire detection.

* `fire_detection_yolo.py` — Fire detection using YOLO model.

* `test_camera.py` — Checks if the camera is functioning.

* HSE illustration image for visual understanding.

📁 Folder Structure

    fire-detection/

    
    ├─ fire_detect_hse.py            # HSV-based fire detection
    
    ├─ fire_detection_yolo.py        # YOLOv8-based fire detection

    ├─ test_camera.py                # Camera Testing
    
    ├─ best.pt                       # Trained YOLO model
    
    ├─ room_fire.mp4                 # Sample video input
    
    ├─ hse_photo.png                 # HSE photo for better understanding
    
    ├─ README.md                     # Project overview
