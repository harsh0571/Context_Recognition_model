# app/vision/detection.py
from ultralytics import YOLO

# Singleton, cache model loading
model = None

def get_model():
    global model
    if model is None:
        model = YOLO('yolov8s.pt')
    return model

def detect_objects(frame):
    model = get_model()
    import numpy as np
    if frame is None or not isinstance(frame, np.ndarray):
        raise ValueError("Frame is not a valid numpy array. Make sure your webcam is working and returns an image.")
    results = model(frame)
    boxes = results[0].boxes
    names = model.names
    labels = [names[int(b.cls[0])] for b in boxes] if len(boxes) else []
    return list(set(labels))
