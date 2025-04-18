import os
import json
import torch
from PIL import Image
from transformers import AutoModelForImageClassification, AutoImageProcessor

def identify_plant(image_path):
    model_path = "models/Medicinal_Plant_Model"
    model = AutoModelForImageClassification.from_pretrained(model_path)
    processor = AutoImageProcessor.from_pretrained(model_path)

    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = logits.argmax(-1).item()

    labels = model.config.id2label
    predicted_plant = labels[predicted_class]

    print(f"\nPredicted Plant: {predicted_plant}")

    benefits_file = "data/benefits.json"
    if not os.path.exists(benefits_file):
        return predicted_plant, ["benefits.json not found!"]

    with open(benefits_file, "r", encoding="utf-8") as f:
        benefits_data = json.load(f)

    matched_plant = None
    for plant_name in benefits_data:
        if predicted_plant in plant_name:
            matched_plant = plant_name
            break

    if matched_plant:
        benefits = benefits_data[matched_plant]["benefits"]
        return predicted_plant, benefits
    else:
        return predicted_plant, ["No medicinal benefits found."]