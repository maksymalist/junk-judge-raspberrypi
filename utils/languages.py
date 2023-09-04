from enum import Enum
from utils.translations import ENGLISH, FRENCH

class Language(Enum):
    EN = 'EN'
    FR = 'FR'

class LanguageDictionary:
    def __init__(self, **kwargs):
        self.dictionaries = kwargs
        
    def __str__(self) -> str:
        return str(self.dictionaries)

    def __getitem__(self, key):
        return self.dictionaries[key]

language_dict = LanguageDictionary(EN=ENGLISH, FR=FRENCH)
print(language_dict)

