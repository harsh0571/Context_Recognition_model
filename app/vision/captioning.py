# app/vision/captioning.py
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import cv2

processor = None
model = None

def load_blip():
    from transformers import BlipProcessor, BlipForConditionalGeneration
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained(
        "Salesforce/blip-image-captioning-base",
        use_safetensors=True,
        trust_remote_code=True
    )
    return processor, model

def get_image_caption(frame):
    processor, model = load_blip()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(img)
    inputs = processor(pil_img, return_tensors="pt")
    out = model.generate(**inputs)
    return processor.decode(out[0], skip_special_tokens=True)
