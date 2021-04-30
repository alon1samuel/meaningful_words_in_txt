import unittest
from src import get_words_only 


class TemplateTest(unittest.TestCase):

    @staticmethod
    def test_gets_words_from_string():
        # Input data and reference
        string_of_words_input = "Alon, guy , ~~: that are not words"
        reference_words_list = ["Alon", "guy", "that", "are", "not", "words"]
        # Check assertion
        assert reference_words_list == get_words_only.gets_words_list_from_string(
            string_of_words_input)

    @staticmethod
    def test_convert_to_lower_letter():
        # Input data and reference
        input_list_words = ["Alon", "guy", "thAt", "aRe", "Not", "words"]
        reference_lower_letter_words = [
            "alon", "guy", "that", "are", "not", "words"]
        # Check assertion
        assert reference_lower_letter_words == get_words_only.convert_to_lower_letter(
            input_list_words)


if __name__ == '__main__':
    unittest.main()
