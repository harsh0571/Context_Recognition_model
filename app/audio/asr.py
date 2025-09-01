# app/audio/asr.py
import streamlit as st
import speech_recognition as sr

def get_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Say something...")
        audio = r.listen(source, phrase_time_limit=5)
    try:
        return r.recognize_google(audio).lower()
    except Exception as e:
        st.warning("Sorry, I couldn't hear you.")
        return ""
