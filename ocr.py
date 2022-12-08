from google.cloud import vision
from pathlib import Path
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "ocr.json"

p = Path(__file__).parent / "sample.jpg"

client = vision.ImageAnnotatorClient()

with p.open("rb") as image_file:
    content = image_file.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)

    print(response.full_text_annotation.text)
