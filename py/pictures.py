import os
from ultralytics import YOLO

# Load a model
model = YOLO("./best.pt")  # load a pretrained model (recommended for training)

#Za jednu sliku
#results = model("/content/gdrive/My Drive/Colab Notebooks/Glass model/data/test/val/images.jpeg")  # predict on an image

#Za više slika od jednom
folder_putanja = "./data/test/val"
slike = os.listdir(folder_putanja)
for slika in slike:
    putanja_do_slike = os.path.join(folder_putanja, slika)
    rezultat = model(putanja_do_slike)