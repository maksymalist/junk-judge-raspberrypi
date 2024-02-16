from utils.prediction import Prediction, TrashType

## SAMPLE OUTPUT ##
# {
#   "result": "trash",
#   "m1_confidence": {
#     "biological": 0.00011916612857021391,
#     "cardboard": 0.6136821508407593,
#     "glass": 0.005561398342251778,
#     "metal": 0.008755425922572613,
#     "paper": 0.3135942220687866,
#     "plastic": 0.05709577351808548,
#     "trash": 0.0011918857926502824
#   },
#   "m2_confidence": {
#     "cardboard": 0.013121964409947395,
#     "glass": 0.032863762229681015,
#     "metal": 0.02823690138757229,
#     "paper": 0.05429587513208389,
#     "plastic": 0.023277077823877335,
#     "trash": 0.8482044339179993
#   },
#   "probabilities": [
#     [
#       0.00011916612857021391,
#       0.6136821508407593,
#       0.005561398342251778,
#       0.008755425922572613,
#       0.3135942220687866,
#       0.05709577351808548,
#       0.0011918857926502824,
#       0.013121964409947395,
#       0.032863762229681015,
#       0.02823690138757229,
#       0.05429587513208389,
#       0.023277077823877335,
#       0.8482044339179993
#     ]
#   ],
#   "embedding_confidence": 0.5217162370681763
# }

def text_to_prediction(text):
    if text == "trash":
        return Prediction.TRASH
    elif text == "biological":
        return Prediction.BIOLOGICAL
    elif text == "recyclable":
        return Prediction.RECYCLABLE
    else:
        raise Exception("not a valid trash type")

def sort_by_type(pred):
    if pred == TrashType.TRASH:
        return Prediction.TRASH
    elif pred == TrashType.BIOLOGICAL:
        return Prediction.BIOLOGICAL
    elif pred == TrashType.PLASTIC or pred == TrashType.METAL or pred == TrashType.CARDBOARD or pred == TrashType.PAPER or pred == TrashType.GLASS:
        return Prediction.RECYCLABLE
    else:
        raise Exception("not a valid trash type")