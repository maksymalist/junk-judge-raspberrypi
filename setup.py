# from src.camera import take_picture
# from src.algo import predict_type
# from src.camera import PATH
# import os
from utils.firebase import upload_file_to_firebase
from utils.notion import create_notion_entry
from src.algo import predict_type

if __name__ == "__main__":
    # take_picture()
    # if not os.path.exists(PATH):
    #     print("No image found.")
    #     exit(1)
        
    # prediction = predict_type()
    # print(prediction)
    # Usage example
    file_path = 'images/test.jpg'
    prediction = predict_type(file_path)
    key, file_size, file_type, file_name, file_url = upload_file_to_firebase(file_path, prediction)

    print('File uploaded successfully.')
    print('File Size:', file_size)
    print('File Type:', file_type)
    print('File Name:', file_name)
    print('File URL:', file_url)
    
    print(create_notion_entry(file_url, prediction, file_type, file_size, key))