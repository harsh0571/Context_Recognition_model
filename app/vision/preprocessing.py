# app/vision/preprocessing.py
# You can put color conversions, image resizing, etc. here.
def to_rgb(frame):
    import cv2
    return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
