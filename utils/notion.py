import requests
from datetime import datetime

def create_image_entry(image_url, type, file_type, size, key):
   res = requests.post("https://junk-judge-web.vercel.app/api/notion/add-image", json={
    "image_url": image_url,
    "type": type,
    "file_type": file_type,
    "size": size,
    "key": key,
   })
   
   return res.json()


def update_judge_status(id, is_open, status, state, version):
   res = requests.post("https://junk-judge-web.vercel.app/api/notion/update-judge-status", json={
      "id": id,
      "is_open": is_open,
      "status": status,
      "state": state,
      "version": version,
   })
   
   return res.json()
   