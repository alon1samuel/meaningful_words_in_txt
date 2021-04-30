import re


def gets_words_list_from_string(file_string: str) -> list:
    list_just_words = re.findall(r'\w+', file_string)
    words_list = [x for x in list_just_words]
    return words_list


def convert_to_lower_letter(words_list):
    lower_letters_words_list = [x.lower() for x in words_list]
    return lower_letters_words_list


def get_words_only_small_letters(file_string: str) -> list:
    return convert_to_lower_letter(gets_words_list_from_string(file_string))


