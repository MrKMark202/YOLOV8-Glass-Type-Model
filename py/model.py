import os
from ultralytics import YOLO

# Load a model
model = YOLO("./best.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="google_colab_config.yaml", epochs=3)  # train the model