import requests
import base64
from PIL import Image
from io import BytesIO
from gradio_client import Client

client = Client("https://maksymalist-junk-judge.hf.space/")

def predict_type(input_path):
    
    result = client.predict(
		input_path,	# str (filepath or URL to image) in 'image' Image component
		api_name="/predict"
    )

    
    return result