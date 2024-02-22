import requests
import base64

API_URL = "https://api-inference.huggingface.co/models/openai/clip-vit-large-patch14"
headers = {"Authorization": "Bearer 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"}

def query(data):
	with open(data["image_path"], "rb") as f:
		img = f.read()
	payload={
		"parameters": data["parameters"],
		"inputs": base64.b64encode(img).decode("utf-8")
	}
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

labels_1 = ["plastic", "biological", "trash", "metal", "cardboard", "paper", "glass"]
#labels_2 = ["trash", "recyclable", "biological"]


# output = query({
#     "image_path": "biological.jpeg",
#     "parameters": {"candidate_labels": labels_1 },
# })
