import firebase_admin
from firebase_admin import credentials, storage
import time

def upload_file_to_firebase(file_path, predict_type):
    # Initialize Firebase Admin SDK
    cred = credentials.Certificate("credentials.json")
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'junk-judge.appspot.com'
    })

    # Upload the file to Firebase Storage
    key = str(int(time.time() * 1000))
    bucket = storage.bucket()
    blob = bucket.blob(f"{predict_type}/{key}")
    blob.upload_from_filename(file_path)
    blob.make_public()

    # Get file metadata
    file_size = blob.size
    file_type = blob.content_type
    file_name = blob.name
    file_url = blob.public_url

    return key, file_size, file_type, file_name, file_url 
    