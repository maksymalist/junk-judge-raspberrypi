from gradio_client import Client
import json

client = Client("https://maksymalist-junk-judge.hf.space/", serialize=False, hf_token="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")

def predict_type(input_path):

    result = client.predict(
		input_path,	# str (filepath or URL to image) in 'image' Image component
		api_name="/predict"
    )


    return result
