import cv2
import numpy as np

def detect_skin_tone(image_path):
    image = cv2.imread(image_path)

    if image is None:
        return "Unknown"

    avg_color = image.mean(axis=0).mean(axis=0)
    r, g, b = avg_color

    if r > 180:
        return "Fair"
    elif r > 140:
        return "Medium"
    else:
        return "Dark"