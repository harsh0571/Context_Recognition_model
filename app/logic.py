# app/logic.py
import streamlit as st
from app.audio.asr import get_voice_input
from app.vision.detection import detect_objects
from app.vision.captioning import get_image_caption
from app.audio.tts import speak

def handle_user_action(mode):
    if mode == "voice":
        st.session_state['listening'] = True
        # Listen for user voice
        query = get_voice_input()
        st.session_state['listening'] = False
        st.write(f"You asked: {query}")
        # Example: respond
        if "object" in query or "context" in query:
            frame = ... # capture frame here (see detection.py for how)
            objs = detect_objects(frame)
            st.write(f"Detected: {objs}")
            caption = get_image_caption(frame)
            st.write(f"Contextual scene: {caption}")
            speak(f"I see: {objs}. Context is: {caption}")
    elif mode == "vision":
        # capture frame
        import cv2
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        if not ret or frame is None:
            st.error("Could not access your webcam or capture a valid frame.")
            return
        objs = detect_objects(frame)
        caption = get_image_caption(frame)
        st.write(f"Detected: {objs}")
        st.write(f"Context: {caption}")
        speak(f"I see: {objs}. Context is: {caption}")
