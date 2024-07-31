import cv2
import mediapipe as mp
import streamlit as st
import numpy as np
import time
st.title('Hand Tracking App')

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

frame_placeholder = st.empty()
fps_text = st.empty()

pTime = 0

while cap.isOpened():
    success, img = cap.read()
    if not success:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 4:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Update Streamlit components
    frame_placeholder.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), channels="RGB")
    fps_text.text(f'FPS: {int(fps)}')

cap.release()

