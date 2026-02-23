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

𝐸
𝐴
𝑅
=
∣
∣
𝑝
2
−
𝑝
6
∣
∣
+
∣
∣
𝑝
3
−
𝑝
5
∣
∣
2
×
∣
∣
𝑝
1
−
𝑝
4
∣
∣
EAR=
2×∣∣p1−p4∣∣
∣∣p2−p6∣∣+∣∣p3−p5∣∣
	​


If:

EAR < 0.22 for 20 consecutive frames

→ User considered Sleeping

🖥️ System Workflow

Capture live video using OpenCV.

Detect face landmarks using MediaPipe.

Extract eye coordinates.

Compute EAR.

If EAR remains below threshold:

Display “SLEEPING!”

Play alarm sound (alarm.mp3)

When eyes reopen:

Stop alarm.

📂 Project Structure
AI-Based-Real-Time-Sleep-State-Detection-System/
│
├── main.py                  # Main application file
├── face_landmarker.task     # MediaPipe model
├── alarm.mp3                # Alarm sound file
├── inspect_mediapipe.py     # MediaPipe inspection utility
├── requirements.txt
└── README.md
🚀 Installation Guide
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

🧪 Technologies Used

Python

OpenCV

MediaPipe Tasks API

NumPy

Tkinter

Pygame

📊 Applications

🚗 Driver Drowsiness Detection

🏭 Industrial Worker Fatigue Monitoring

🏥 Healthcare Monitoring

🛡️ Safety-Critical Environments

🔮 Future Improvements

Add sound volume control

Add blink rate analytics

Add sleep duration tracking

Deploy as desktop executable (.exe)

Integrate cloud logging system

Add machine learning-based classification

👨‍💻 Author

Ganesh Jadhav
AI & Machine Learning Enthusiast
