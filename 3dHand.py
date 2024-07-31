import cv2
import mediapipe as mp
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import numpy as np
import time
import av

# Define the HandTrackingProcessor class
class HandTrackingProcessor(VideoProcessorBase):
    def __init__(self):
        self.hands = mp.solutions.hands.Hands()
        self.mpDraw = mp.solutions.drawing_utils
        self.pTime = 0

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)
        
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(img, handLms, mp.solutions.hands.HAND_CONNECTIONS)

        cTime = time.time()
        fps = 1 / (cTime - self.pTime)
        self.pTime = cTime

        # Optionally, you can add FPS text to the image
        cv2.putText(img, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        return av.VideoFrame.from_ndarray(img, format="bgr24")

# Define the main function for Streamlit
def main():
    st.set_page_config(page_title="Hand Tracking App", layout="wide")
    
    st.title("Hand Tracking App")
    
    # Video Stream
    webrtc_streamer(
        key="hand-tracking",
        video_processor_factory=HandTrackingProcessor,
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
        media_stream_constraints={"video": True, "audio": False}
    )
    

if __name__ == "__main__":
    main()
