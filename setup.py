from src.camera import take_picture
from src.algo import predict_type
from src.camera import PATH
import os

if __name__ == "__main__":
    take_picture()
    if not os.path.exists(PATH):
        print("No image found.")
        exit(1)
        
    prediction = predict_type()
    print(prediction)