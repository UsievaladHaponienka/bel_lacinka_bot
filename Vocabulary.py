AFTER_VOWEL_KEY = "after_vowel"
AFTER_CONSONANT_KEY = "after_consonant"

__basic_vocabulary = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "h",
    "д": "d",
    "ж": "ž",
    "з": "z",
    "і": "i",
    "й": "j",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "ch",
    "ц": "c",
    "ч": "č",
    "ш": "š",
    "ў": "ǔ",
    "ь": "",
    "ы": "y",
    "э": "e",
}

__vowel_list = [
    "а", "я", "о", "ё", "ы", "і", "у", "ю", "э", "е"
]

__iotated_list = ["я", "ё", "ю", "е"]

__iotated_vocabulary = {
    AFTER_VOWEL_KEY: {
        "е": "je",
        "ё": "jo",
        "ю": "ju",
        "я": "ja",
    },
    AFTER_CONSONANT_KEY: {
        "е": "ie",
        "ё": "io",
        "ю": "iu",
        "я": "ia",
    }
}

def get_basic_vocabulary():
    return __basic_vocabulary

def get_iotated_vocabulary():
    return __iotated_vocabulary

def get_vowel_list():
    return __vowel_list

def get_iotated_list():
    return __iotated_list
