import unittest
from src import get_words_only 


class TemplateTest(unittest.TestCase):

    @staticmethod
    def test_function_gets_words_from_string_return_words_normal_words():
        # Input data and reference
        string_of_words_input = "Alon is a nice guy"
        reference_words_list = ["Alon", "is", "a", "nice", "guy"]
        # Check assertion
        reference_words_list == get_words_only.gets_words_list_from_string(
            string_of_words_input)

    @staticmethod
    def test_function_gets_words_from_string_doesnt_return_lone_punctuations():
        # Input data and reference
        string_of_words_input = ", ~~:"
        reference_words_list = []
        # Check assertion
        reference_words_list == get_words_only.gets_words_list_from_string(
            string_of_words_input)

    @staticmethod    
    def test_function_gets_words_from_string_return_words_without_punctuations():
        # Input data and reference
        string_of_words_input = "Alon, is: a nice guy"
        reference_words_list = ["Alon", "is", "a", "nice", "guy"]
        # Check assertion
        reference_words_list == get_words_only.gets_words_list_from_string(
            string_of_words_input)

    @staticmethod
    def test_convert_to_lower_case_words():
        # Input data and reference
        input_list_words = ["Alon", "guy", "thAt", "aRe", "Not", "words"]
        reference_lower_case_words = [
            "alon", "guy", "that", "are", "not", "words"]
        # Check assertion
        assert reference_lower_case_words == get_words_only.convert_to_lower_case_words(
            input_list_words)


if __name__ == '__main__':
    string_of_words_input = "Alon, is: a nice guy"
    reference_words_list = ["Alon", "is", "a", "nice", "guy"]
    # Check assertion
    assert reference_words_list == get_words_only.gets_words_list_from_string(
        string_of_words_input)
    unittest.main()
