from enum import Enum
from utils.translations import ENGLISH, FRENCH

class Language(Enum):
    EN = 'EN'
    FR = 'FR'

class LanguageDictionary:
    def __init__(self, *dictionaries):
        self.dictionaries = {lang: dictionary for lang, dictionary in dictionaries}

    def __getitem__(self, key):
        return self.dictionaries[key]

language_dict = LanguageDictionary(ENGLISH, FRENCH)

