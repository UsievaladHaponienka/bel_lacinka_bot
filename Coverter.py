import Vocabulary


def resolve_iotated(letter, previous_letter):
    if previous_letter in Vocabulary.get_vowel_list() or previous_letter in Vocabulary.get_j_required_list():
        return Vocabulary.get_iotated_vocabulary()[Vocabulary.AFTER_VOWEL_KEY][letter]
    else:
        return Vocabulary.get_iotated_vocabulary()[Vocabulary.AFTER_CONSONANT_KEY][letter]


def resolve_soft_sign(message):
    letter_to_make_soft = message[-1]
    correct_letter = Vocabulary.get_soft_sign_vocabulary()[letter_to_make_soft]
    message = message[:-1] + correct_letter

    return message


def convert(message):
    new_message = ''
    previous_letter = ''

    for letter in message:
        is_upper = letter.isupper()
        if is_upper:
            letter = letter.lower()

        if letter in Vocabulary.get_basic_vocabulary().keys():
            letter_to_add = Vocabulary.get_basic_vocabulary()[letter]
        elif letter in Vocabulary.get_iotated_list():
            letter_to_add = resolve_iotated(letter, previous_letter)
        elif letter == Vocabulary.SOFT_SIGN:
            new_message = resolve_soft_sign(new_message)
            continue
        else:
            letter_to_add = letter

        if is_upper:
            if len(letter_to_add) == 1:
                letter_to_add = letter_to_add.upper()
            else:
                letter_to_add = letter_to_add[0].upper() + letter_to_add[1:]

        new_message += letter_to_add
        previous_letter = letter

    return new_message