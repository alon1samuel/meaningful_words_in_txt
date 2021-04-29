import re
from src.utils import SaveRead


def gets_words_from_string(file_string: str) -> list:
    list_just_words = re.findall(r'\w+', file_string)
    list_words_small_letters = [x for x in list_just_words]
    return list_words_small_letters


def convert_to_lower_letter(words_list):
    lower_letters_words_list = [x.lower() for x in words_list]
    return lower_letters_words_list


def get_number_of_words_from_file(file_path):
    file_string = SaveRead.read_txt_file_to_string(file_path)
    lower_letters_words_list = get_words_only_small_letters(file_string)
    return len(lower_letters_words_list)


def get_words_only_small_letters(file_string: str) -> list:
    return convert_to_lower_letter(gets_words_from_string(file_string))
