import requests
from datetime import datetime

def create_notion_entry(image_url, type, file_type, size, key):
   res = requests.post("https://junk-judge-web.vercel.app/api/notion/add-image", json={
    "image_url": image_url,
    "type": type,
    "file_type": file_type,
    "size": size,
    "key": key,
   })
   
   return res.json()