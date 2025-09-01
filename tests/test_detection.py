# tests/test_detection.py
from app.vision.detection import detect_objects

def test_detect_objects():
    # You'd provide a test frame here for CI
    assert isinstance(detect_objects(...), list)
