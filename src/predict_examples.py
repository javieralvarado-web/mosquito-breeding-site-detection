from ultralytics import YOLO
from pathlib import Path

MODEL_PATH = "/home/javier/Javier_Alvarado_Proyecto/best.pt"
IMAGE_DIR = "/home/javier/Javier_Alvarado_Proyecto/dataset/inferencias"
OUTPUT_DIR = "/home/javier/Javier_Alvarado_Proyecto/results"

model = YOLO(MODEL_PATH)

results = model.predict(
    source=IMAGE_DIR,
    save=True,
    project=".",
    name="predictions",
    exist_ok=True,
    conf=0.4
)

print(f"Resultados guardados en: {OUTPUT_DIR}")