import unittest
from src import find_meaningful_words
from src.utils import SaveRead
import os

DATA_DIR = "tests/data_tests"

class PipelineTests(unittest.TestCase):

    @staticmethod
    def test_hamlet_meaningful_words():
        """Testing hamlet meaningful words whole pipeline.
        """
        
        # Read test data
        pipeline_data_name = "pipeline_data.pkl"
        pipeline_data_path = os.path.join(DATA_DIR, pipeline_data_name)
        ref_hamlet_words_number, ref_hamlet_most_common_words, ref_hamlet_meaningful_words = SaveRead().read_data_pickle(path_to_read=pipeline_data_path)

        # Activating hamlet meaningful words pipeline.
        hamlet_words_number, hamlet_most_common_words, hamlet_meaningful_words = find_meaningful_words.main(print_results=False)

        # Assertion
        assert hamlet_words_number == ref_hamlet_words_number
        assert hamlet_most_common_words == ref_hamlet_most_common_words
        assert hamlet_meaningful_words == ref_hamlet_meaningful_words


    
if __name__ == '__main__':
    unittest.main()