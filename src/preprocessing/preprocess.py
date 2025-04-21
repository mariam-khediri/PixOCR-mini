# src/preprocessing/preprocess.py

import cv2
import numpy as np
import pytesseract
from PIL import Image
import requests
from io import BytesIO

def load_image(img_path):
    if img_path.startswith("http"):
        response = requests.get(img_path)
        image = Image.open(BytesIO(response.content)).convert("RGB")
    else:
        image = Image.open(img_path).convert("RGB")
    return np.array(image)

def preprocess_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def preprocess_adaptive_threshold(img):
    gray = preprocess_grayscale(img)
    return cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                 cv2.THRESH_BINARY, 11, 2)

def preprocess_inverted(img):
    gray = preprocess_grayscale(img)
    return cv2.bitwise_not(gray)

def preprocess_color_mask(img, color="green"):
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    if color == "green":
        lower, upper = (36, 25, 25), (86, 255, 255)
    elif color == "white":
        lower, upper = (0, 0, 200), (180, 30, 255)
    else:
        raise ValueError("Unsupported color")
    mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
    return cv2.bitwise_and(img, img, mask=mask)

def run_ocr(img):
    if len(img.shape) == 2:
        return pytesseract.image_to_string(img)
    return pytesseract.image_to_string(cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

def ocr_pipeline(img_path):
    img = load_image(img_path)
    methods = {
        "grayscale": preprocess_grayscale,
        "adaptive_threshold": preprocess_adaptive_threshold,
        "inverted": preprocess_inverted,
        "color_mask_green": lambda x: preprocess_color_mask(x, "green"),
        "color_mask_white": lambda x: preprocess_color_mask(x, "white")
    }
    results = {}
    for name, method in methods.items():
        try:
            processed = method(img)
            text = run_ocr(processed)
            results[name] = text
        except Exception as e:
            results[name] = f"Error: {e}"
    return results
