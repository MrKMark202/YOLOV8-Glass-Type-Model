import os
from ultralytics import YOLO

# Create a new model
# model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Load a model
model = YOLO("./best.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="google_colab_config.yaml", epochs=3)  # train the model