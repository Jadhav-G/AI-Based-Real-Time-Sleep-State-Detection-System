🧠 AI-Based Real-Time Sleep State Detection System
📌 Project Overview

The AI-Based Real-Time Sleep State Detection System is a real-time computer vision application that detects drowsiness using facial landmarks and Eye Aspect Ratio (EAR) analysis.

The system uses:

MediaPipe Face Landmarker

OpenCV

NumPy

Tkinter GUI

Pygame (for alarm system)

When prolonged eye closure is detected, the system triggers an audio alarm to alert the user.

🎯 Key Features

✅ Real-time webcam monitoring

✅ MediaPipe Face Landmark detection

✅ Eye Aspect Ratio (EAR) based sleep detection

✅ Configurable threshold logic

✅ Automatic alarm trigger using pygame

✅ Modern futuristic GUI built with Tkinter

✅ Start / Stop monitoring controls

🏗️ Project Architecture
🔹 1. Face Detection

Uses MediaPipe FaceLandmarker model:

face_landmarker.task

🔹 2. Eye Aspect Ratio (EAR) Calculation

Eye landmarks used:

LEFT_EYE → [33, 160, 158, 133, 153, 144]

RIGHT_EYE → [362, 385, 387, 263, 373, 380]

EAR Formula:
EAR = (||p2 - p6|| + ||p3 - p5||) / (2 × ||p1 - p4||)

Sleep Detection Condition:

EAR < 0.22 for 20 consecutive frames​

→ User considered Sleeping

🖥️ System Workflow

1. Capture live video using OpenCV.

2. Detect face landmarks using MediaPipe.

3. Extract eye coordinates.

4. Compute EAR.

5. If EAR remains below threshold:

    - Display “SLEEPING!”

    - Play alarm sound (alarm.mp3)

6. When eyes reopen:

   -Stop alarm.



🚀 Installation Guide :

1️⃣ Clone Repository
git clone https://github.com/Jadhav-G/AI-Based-Real-Time-Sleep-State-Detection-System.git
cd AI-Based-Real-Time-Sleep-State-Detection-System

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install opencv-python mediapipe numpy pygame

Or using requirements file:

pip install -r requirements.txt

4️⃣ Run the Application
python main.py
⚙️ Configuration Parameters

Inside main.py:

EAR_THRESHOLD = 0.22
FRAME_THRESHOLD = 20

You can adjust:

EAR sensitivity

Number of consecutive frames




##👨‍💻 Author

##Ganesh Namdev Jadhav

AI & Machine Learning Enthusiast
