import re


def gets_words_list_from_string(file_string: str) -> list:
    list_just_words = re.findall(r'\w+', file_string)
    words_list = [x for x in list_just_words]
    return words_list


def convert_to_lower_case_words(words_list):
    lower_case_words_list = [x.lower() for x in words_list]
    return lower_case_words_list


def get_words_in_lower_case(file_string: str) -> list:
    return convert_to_lower_case_words(gets_words_list_from_string(file_string))


