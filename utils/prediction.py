from enum import Enum

class Prediction(Enum):
    TRASH = 0
    RECYCLABLE = 1
    BIOLOGICAL = 2
    
class TrashType(Enum):
    TRASH = 0
    BIOLOGICAL = 1
    PLASTIC = 2
    METAL = 3
    CARDBOARD = 4
    PAPER = 5
    GLASS = 6
        

def trash(s):
    if s == "trash":
        return TrashType.TRASH
    elif s == "biological":
        return TrashType.BIOLOGICAL
    elif s == "plastic":
        return TrashType.PLASTIC
    elif s == "metal":
        return TrashType.METAL
    elif s == "cardboard":
        return TrashType.CARDBOARD
    elif s == "paper":
        return TrashType.PAPER
    elif s == "glass":
        return TrashType.GLASS
    else:
        raise Exception("not a valid trash type")