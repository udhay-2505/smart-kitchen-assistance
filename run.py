# -*- coding: utf-8 -*-
"""run.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vrsp34UB-Whw-HwabuM6VvSQH52zzAXM
"""

import cv2
import torch
from ultralytics import YOLO
from google.colab.patches import cv2_imshow  # Use for Colab

# Load YOLO model
model_path = "/content/best.pt"
source = "/content/chicken.jpg"

model = YOLO(model_path)

# Detect objects
results = model(source)

# Draw bounding boxes
if source.endswith(('.jpg', '.jpeg', '.png')):
    for result in results:
        frame = result.plot()
        cv2_imshow(frame)
elif source.endswith(('.mp4', '.avi')):
    cap = cv2.VideoCapture(source)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame)
        for result in results:
            frame = result.plot()
        cv2_imshow(frame)
    cap.release()

!pip install ultralytics