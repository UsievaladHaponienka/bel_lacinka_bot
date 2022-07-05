AFTER_VOWEL_KEY = "after_vowel"
AFTER_CONSONANT_KEY = "after_consonant"
SOFT_SIGN = 'ь'

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
    "ы": "y",
    "э": "e",
}

__vowel_list = [
    "а", "я", "о", "ё", "ы", "і", "у", "ю", "э", "е"
]

__iotated_list = ["я", "ё", "ю", "е"]

__j_required_list = ["", " ", "ў", "'"]

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

__soft_sign_vocabulary = {
    "z": "ź",
    "l": "ĺ",
    "n": "ń",
    "s": "ś",
    "c": "ć"
}

def get_basic_vocabulary():
    return __basic_vocabulary

def get_iotated_vocabulary():
    return __iotated_vocabulary

def get_vowel_list():
    return __vowel_list

def get_iotated_list():
    return __iotated_list

def get_soft_sign_vocabulary():
    return __soft_sign_vocabulary

def get_j_required_list():
    return __j_required_list