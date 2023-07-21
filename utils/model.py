import requests
from PIL import Image
import io
import base64

def img_to_base64(img_path):
    pil_image = Image.open(img_path)
    buffered = io.BytesIO()
    pil_image.save(buffered, format="JPEG")  # You can change the format if needed (JPEG, PNG, etc.)
    base64_encoded = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return base64_encoded

def predict_type(input_path):
  
    item = {
        "image_b64": img_to_base64(input_path)
    }

    response = requests.post(
      "https://junk-judge-web.vercel.app/api/predict", 
      json=item, 
    headers={
      "Content-Type": "application/json"
    },
    timeout=10
    )
    
    return response.json()
