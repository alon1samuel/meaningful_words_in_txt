from collections import Counter
from src.config import config

def count_occurences_of_elements_in_a_list(elements: list)-> list:
    counted_words_dict = dict(
        Counter(elements))
    counted_elements_in_tuple_list = list(counted_words_dict.items())
    return counted_elements_in_tuple_list 


def sort_elements_and_occurences_tuple_list_from_high_to_low(counted_words_tuple_list):
    sorted_counted_words_tuple_list = sorted(
        counted_words_tuple_list, key=lambda x: 
        x[config.COUNT_PLACE_IN_WORDS_COUNT_LIST], reverse=True)
    return sorted_counted_words_tuple_list


def words_count_to_words_list(words_count_tuple_list):
    return [x[config.WORDS_PLACE_IN_WORDS_COUNT_LIST] for x in words_count_tuple_list]


def words_count_to_count_list(words_count_tuple_list):
    return [x[config.COUNT_PLACE_IN_WORDS_COUNT_LIST] for x in words_count_tuple_list]


def get_first_words_in_tuple_list(words_count_tuple_list, number_of_words):
    words_list = words_count_to_words_list(words_count_tuple_list)
    first_words_list = words_list[:number_of_words]
    return first_words_list 
