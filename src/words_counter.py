from collections import Counter
from src.config import config

def sort_words_count(counted_words_tuple_list):
    sorted_counted_words_tuple_list = sorted(
        counted_words_tuple_list, key=lambda x: 
        x[config.FREQUENCY_PLACE_IN_FREQUENCY_LIST], reverse=True)
    return sorted_counted_words_tuple_list


def count_words_in_list(words_list):
    counted_words_dict = dict(
        Counter(words_list))
    counted_words_tuple_list = counted_words_dict.items()
    sorted_counted_words_tuple_list = sort_words_count(
        counted_words_tuple_list)
    return sorted_counted_words_tuple_list


def get_only_common_words(words_frequencies_dict, number_of_most_common):
    return [x[config.WORDS_PLACE_IN_WORDS_COUNT_LIST] 
        for x in words_frequencies_dict[:number_of_most_common]]
