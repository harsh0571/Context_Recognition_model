import streamlit as st
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from app.ui import show_main_page

def main():
    st.set_page_config(page_title="AI Avatar Vision", page_icon="💬")
    show_main_page()

if __name__ == "__main__":
    main()
