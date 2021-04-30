from src.utils import SaveRead
from src import get_words_only, words_counter, ratio_of_words_count


# TODO: Add documentation to each function.
# TODO: Add tests to each function
# TODO: Divide function into different files.
# TODO: Add configuration file for magic numbers and strings.

def count_words_from_file(file_path):
    file_string = SaveRead.read_txt_file_to_string(file_path)
    lower_letters_words_list = get_words_only.get_words_only_small_letters(file_string)
    words_count = len(lower_letters_words_list) 
    return words_count



def get_most_common_words_in_string(file_path, number_of_most_common):

    file_string = SaveRead.read_txt_file_to_string(file_path)
    only_words_list = get_words_only.get_words_only_small_letters(file_string)
    counted_words_tuple_list = words_counter.count_words_in_list(only_words_list)
    most_common_words = words_counter.get_only_common_words(
        counted_words_tuple_list, number_of_most_common)
    return most_common_words


def find_meaningful_words_in_file_from_another_file(base_path, reference_path, number_of_words):
    # Count words in base and reference files
    base_words_counted = words_counter.count_words_in_list(
        get_words_only.get_words_only_small_letters(SaveRead.read_txt_file_to_string(base_path)))
    reference_words_counted = words_counter.count_words_in_list(
        get_words_only.get_words_only_small_letters(SaveRead.read_txt_file_to_string(reference_path)))
    # Get the ratio of base words count relative to reference words count.
    base_words_relative_reference_count_tuple_list = \
        ratio_of_words_count.get_ratio_of_base_words_count_relative_to_reference_words_count(
        base_words_counted, reference_words_counted)
    # Sort the relative count of base words
    sorted_base_words_relative_reference_count_tuple_list = words_counter.sort_words_count(
        base_words_relative_reference_count_tuple_list)
    most_meaningful_words = words_counter.get_only_common_words(
        sorted_base_words_relative_reference_count_tuple_list, number_of_words)
    return most_meaningful_words


def main(print_results=True):
    hamlet_path = "hamlet.txt"
    # Find how many words are there in hamlet txt file.
    hamlet_words_number = count_words_from_file(hamlet_path)
    if print_results:
        print(f"There are {hamlet_words_number} words in hamlet play.")

    # Find the 30 most common words.
    hamlet_path = "hamlet.txt"
    how_many_common_words = 30
    hamlet_most_common_words = get_most_common_words_in_string(
        hamlet_path, how_many_common_words)
    if print_results:
        print(
            f"The {how_many_common_words} most common words in hamlet are - {hamlet_most_common_words}")

    # Having macbeth txt, could you find the most meaningful words in the hamlet file.
    hamlet_path = "hamlet.txt"
    macbeth_path = "macbeth.txt"
    how_many_common_words = 30
    hamlet_meaningful_words = find_meaningful_words_in_file_from_another_file(
        hamlet_path, macbeth_path, how_many_common_words)
    if print_results:
        print(
            f"These are the most meaningful words in the hamlet play: {hamlet_meaningful_words}")

    return hamlet_words_number, hamlet_most_common_words, hamlet_meaningful_words


if __name__ == "__main__":
    main()
