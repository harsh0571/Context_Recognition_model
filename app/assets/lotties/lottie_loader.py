# app/assets/lottie_loader.py
import json
import os

def load_lottie(path):
    with open(path, "r") as f:
        return json.load(f)
