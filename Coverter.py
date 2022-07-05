import Vocabulary


class Converter:

    def resolve_iotated(self, letter, previous_letter):
        if (previous_letter in Vocabulary.get_vowel_list()) or previous_letter == " ":
            return Vocabulary.get_iotated_vocabulary()[Vocabulary.AFTER_VOWEL_KEY][letter]
        else:
            return Vocabulary.get_iotated_vocabulary()[Vocabulary.AFTER_CONSONANT_KEY][letter]

    def convert(self, message):
        new_message = ''
        previous_letter = ''

        for letter in message:
            is_upper = letter.isupper()
            if is_upper:
                letter = letter.lower()

            if letter in Vocabulary.get_basic_vocabulary().keys():
                letter_to_add = Vocabulary.get_basic_vocabulary()[letter]
            elif letter in Vocabulary.get_iotated_list():
                letter_to_add = self.resolve_iotated(letter, previous_letter)
            else:
                letter_to_add = letter

            if is_upper:
                letter_to_add = letter_to_add.upper()

            new_message += letter_to_add
            previous_letter = letter

        return new_message
