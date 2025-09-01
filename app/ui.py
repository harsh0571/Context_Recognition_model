# app/ui.py
import streamlit as st
from streamlit_lottie import st_lottie
from assets.lottie_loader import load_lottie_url
from logic import handle_user_action

def show_main_page():
    # Load the chatbot avatar Lottie
    avatar = load_lottie_url("https://lottie.host/5f986ab4-500f-43f3-b662-f2f1a3de4528/Noy35maAkp.json")  # Changed load_lottie to load_lottie_url
    st_lottie(avatar, height=200, key="avatar", speed=1)

    st.title("🤖 AI Avatar Vision Assistant")
    st.markdown("What do you want to know?")

    # Example user actions: voice button, click, etc.
    if st.button("Ask with Voice"):
        handle_user_action("voice")
    if st.button("What objects/context are in the frame?"):
        handle_user_action("vision")
