import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import tkinter as tk
import threading
import pygame

pygame.mixer.init()

MODEL_PATH = "face_landmarker.task"

BaseOptions = python.BaseOptions
FaceLandmarker = vision.FaceLandmarker
FaceLandmarkerOptions = vision.FaceLandmarkerOptions
VisionRunningMode = vision.RunningMode

options = FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=MODEL_PATH),
    running_mode=VisionRunningMode.IMAGE,   # ✅ CHANGED
    num_faces=1
)

landmarker = FaceLandmarker.create_from_options(options)

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

EAR_THRESHOLD = 0.22
FRAME_THRESHOLD = 20

running = False


def play_alarm():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load("alarm.mp3")
        pygame.mixer.music.play(-1)  # loop until stopped


def stop_alarm():
    pygame.mixer.music.stop()


def eye_aspect_ratio(eye, landmarks, w, h):
    points = []
    for idx in eye:
        x = int(landmarks[idx].x * w)
        y = int(landmarks[idx].y * h)
        points.append((x, y))

    A = np.linalg.norm(np.array(points[1]) - np.array(points[5]))
    B = np.linalg.norm(np.array(points[2]) - np.array(points[4]))
    C = np.linalg.norm(np.array(points[0]) - np.array(points[3]))

    return (A + B) / (2.0 * C)


def detect_sleep():
    global running

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # ✅ Windows fix
    counter = 0

    while running:
        ret, frame = cap.read()
        if not ret:
            print("Camera not working")
            break

        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
        result = landmarker.detect(mp_image)   # ✅ CHANGED

        if result.face_landmarks:
            landmarks = result.face_landmarks[0]

            left_ear = eye_aspect_ratio(LEFT_EYE, landmarks, w, h)
            right_ear = eye_aspect_ratio(RIGHT_EYE, landmarks, w, h)
            ear = (left_ear + right_ear) / 2

            if ear < EAR_THRESHOLD:
                counter += 1
                if counter >= FRAME_THRESHOLD:
                    cv2.putText(frame, "SLEEPING!", (50, 100),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.5,
                                (0, 0, 255), 3)
                    play_alarm()
            else:
                counter = 0
                stop_alarm()

        cv2.imshow("Sleep Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            running = False
            break

    cap.release()
    cv2.destroyAllWindows()


def start_detection():
    global running
    if not running:
        running = True
        threading.Thread(target=detect_sleep).start()


def stop_detection():
    global running
    running = False
    stop_alarm()
    cv2.destroyAllWindows()


# ---------------- GUI ---------------- #

# root = tk.Tk()
# root.title("Sleep Detection System")
# root.geometry("400x250")

# tk.Label(root, text="Sleep Detection Alarm System",
#          font=("Arial", 14, "bold")).pack(pady=20)

# tk.Button(root, text="Start Detection",
#           command=start_detection,
#           bg="green", fg="white",
#           width=20).pack(pady=10)

# tk.Button(root, text="Stop Detection",
#           command=stop_detection,
#           bg="red", fg="white",
#           width=20).pack(pady=10)

# tk.Button(root, text="Exit",
#           command=root.quit,
#           width=20).pack(pady=10)

# root.mainloop()


# ---------------- Modern Futuristic GUI ---------------- #

root = tk.Tk()
root.title("AI Sleep Detection System")
root.geometry("520x480")
root.configure(bg="#0f0f1a")
root.resizable(False, False)

title = tk.Label(
    root,
    text="AI Sleep Detection",
    font=("Segoe UI", 22, "bold"),
    fg="#00f5ff",
    bg="#0f0f1a"
)
title.pack(pady=(30, 5))

subtitle = tk.Label(
    root,
    text="Real-Time Drowsiness Monitoring System",
    font=("Segoe UI", 10),
    fg="#aaaaaa",
    bg="#0f0f1a"
)
subtitle.pack(pady=(0, 30))


status_label = tk.Label(
    root,
    text="System Status: Idle",
    font=("Segoe UI", 11),
    fg="#ffcc00",
    bg="#0f0f1a"
)
status_label.pack(pady=10)


def styled_button(text, command, color):
    return tk.Button(
        root,
        text=text,
        command=command,
        font=("Segoe UI", 12, "bold"),
        bg=color,
        fg="white",
        activebackground="#1f1f2e",
        activeforeground="white",
        bd=0,
        width=18,
        height=2,
        cursor="hand2"
    )


def start_ui():
    status_label.config(text="System Status: Monitoring...", fg="#00ff99")
    start_detection()


def stop_ui():
    status_label.config(text="System Status: Stopped", fg="#ff4444")
    stop_detection()


start_btn = styled_button("Start Detection", start_ui, "#00b894")
start_btn.pack(pady=15)

stop_btn = styled_button("Stop Detection", stop_ui, "#d63031")
stop_btn.pack(pady=15)

exit_btn = styled_button("Exit System", root.quit, "#6c5ce7")
exit_btn.pack(pady=25)


footer = tk.Label(
    root,
    text="Powered by Ganesh ",
    font=("Segoe UI", 8),
    fg="#555555",
    bg="#0f0f1a"

)
start_btn.pack(pady=15)
stop_btn.pack(pady=15)
exit_btn.pack(pady=20)

# footer.pack(side="bottom", pady=10)

footer.pack(side="bottom", pady=10)

root.mainloop()
