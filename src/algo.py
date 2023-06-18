import requests
from camera import PATH
import base64
from PIL import Image
from io import BytesIO

def predict_type():
    
    image = Image.open(PATH)
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    base64_image = base64.b64encode(buffered.getvalue())
    
    print(base64_image)
    
    req = requests.post("https://junk-judge-web.vercel.app/api/predict", 
        json={
        "image_b64": base64_image.decode("utf-8")
    }, headers={
        "Content-Type": "application/json",
    })
    
    print(req.json())