import requests

def img_to_base64(img_path):
    with open(img_path, "rb") as f:
        return f.read().encode("base64")

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
