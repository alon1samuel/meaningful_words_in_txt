import unittest
from src import words_counter

class WordsCounterTests(unittest.TestCase):

    @staticmethod
    def test_count_words_in_list():
        words_list = ['alon', 'alon', 'avi', "avi", "avi", "d", "alon", "avi"]
        reference_words_count_tuple_list = [('alon', 3), ('avi', 4), ('d', 1)]
        assert reference_words_count_tuple_list == \
            words_counter.count_words_in_list(words_list)
        pass

    @staticmethod
    def test_sort_words_count():
        words_count_tuple_list = [('alon', 9), ('what', 20), ('cools', 3), ('abbi', 6)]
        reference_sorted_words_count_tuple_list = [('what', 20), ('alon', 9), ('abbi', 6) , ('cools', 3)]
        assert reference_sorted_words_count_tuple_list == \
            words_counter.sort_words_count(words_count_tuple_list)

    @staticmethod
    def test_get_first_words_in_tuple_list():
        words_count_tuple_list = [('alon', 9), ('what', 20), ('cools', 3), ('abbi', 6)]
        number_of_words = 3
        reference_first_words_list = ['alon', 'what', 'cools']
        assert reference_first_words_list == words_counter.get_first_words_in_tuple_list(words_count_tuple_list, number_of_words)



if __name__ == '__main__':
    unittest.main()
