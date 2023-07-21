from gradio_client import Client
import json

client = Client("https://maksymalist-junk-judge.hf.space/", serialize=True, hf_token="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")

def predict_type(input_path):
    # Send the file data directly without serialization
    with open(input_path, 'rb') as file:
        result = client.predict(
            file,               # File data to be sent
            api_name="/predict"
        )
    return result
