from collections import Counter
from src.utils import SaveRead
from src.count_words import get_words_only_small_letters, count_words_from_file

#
WORDS_PLACE_IN_FREQUENCY_LIST = 0
FREQUENCY_PLACE_IN_FREQUENCY_LIST = 1

# TODO: Add documentation to each function.
# TODO: Add tests to each function
# TODO: Divide function into different files.
# TODO: Add configuration file for magic numbers and strings.


def sort_words_count(counted_words_tuple_list):
    sorted_counted_words_tuple_list = sorted(
        counted_words_tuple_list, key=lambda x: x[FREQUENCY_PLACE_IN_FREQUENCY_LIST], reverse=True)
    return sorted_counted_words_tuple_list


def count_words_in_list(words_list):
    counted_words_dict = dict(Counter(words_list))
    counted_words_tuple_list = counted_words_dict.items()
    sorted_counted_words_tuple_list = sort_words_count(
        counted_words_tuple_list)
    return sorted_counted_words_tuple_list


def get_only_common_words(words_frequencies_dict, number_of_most_common):
    return [x[WORDS_PLACE_IN_FREQUENCY_LIST] for x in words_frequencies_dict[:number_of_most_common]]


def get_most_common_words_in_string(file_path, number_of_most_common):

    file_string = SaveRead.read_txt_file_to_string(file_path)
    only_words_list = get_words_only_small_letters(file_string)
    counted_words_tuple_list = count_words_in_list(only_words_list)
    most_common_words = get_only_common_words(
        counted_words_tuple_list, number_of_most_common)
    return most_common_words


def turn_words_count_tuple_list_to_words_only(frequencies_list):
    return [x[WORDS_PLACE_IN_FREQUENCY_LIST] for x in frequencies_list]


def add_missing_base_words_to_reference_words_count(base_words, reference_words, reference_frequencies):
    base_words_not_in_ref = set(base_words) ^ set(reference_words)
    reference_counted_words_and_base_words = reference_frequencies + \
        [(x, 1) for x in base_words_not_in_ref]
    return reference_counted_words_and_base_words


def get_base_words_with_reference_count(base_words_list, reference_words_list, reference_words_count_tuple_list):
    reference_words_count_with_base_words_addition = add_missing_base_words_to_reference_words_count(
        base_words_list, reference_words_list, reference_words_count_tuple_list)
    joint_reference_base_words_list = turn_words_count_tuple_list_to_words_only(
        reference_words_count_with_base_words_addition)
    # Find the index of words from base list to reference
    base_words_index_in_joint_reference_words_list = [joint_reference_base_words_list.index(
        x) for x in base_words_list]
    # Get base words with reference count
    base_words_with_reference_count = [reference_words_count_with_base_words_addition[x]
                                       for x in base_words_index_in_joint_reference_words_list]
    return base_words_with_reference_count


def calculate_relative_words_count_of_2_lists(base_words_count_tuple_list, base_words_with_reference_count):
    range_base_words = range(len(base_words_count_tuple_list))
    # For each word in base list, calculate the relative count to the reference words list
    base_relative_to_reference_count = [base_words_count_tuple_list[x][FREQUENCY_PLACE_IN_FREQUENCY_LIST] /
                                        base_words_with_reference_count[x][FREQUENCY_PLACE_IN_FREQUENCY_LIST]
                                        for x in range_base_words]
    # Create a words_ count tuple list
    base_words_relative_reference_count_tuple_list = [
        (base_words_count_tuple_list[x][WORDS_PLACE_IN_FREQUENCY_LIST], 
        base_relative_to_reference_count[x]) 
        for x in range_base_words]
    return base_words_relative_reference_count_tuple_list


def get_ratio_of_base_words_count_relative_to_reference_words_count(base_words_count_tuple_list,
                                                                    reference_words_count_tuple_list):
    base_words_list = turn_words_count_tuple_list_to_words_only(
        base_words_count_tuple_list)
    reference_words_list = turn_words_count_tuple_list_to_words_only(
        reference_words_count_tuple_list)
    base_words_with_reference_count = get_base_words_with_reference_count(
        base_words_list, reference_words_list, reference_words_count_tuple_list)
    base_words_relative_reference_count_tuple_list = calculate_relative_words_count_of_2_lists(
        base_words_count_tuple_list, base_words_with_reference_count)

    return base_words_relative_reference_count_tuple_list


def find_meaningful_words_in_file_from_another_file(base_path, reference_path, number_of_words):
    # Count words in base and reference files
    base_words_counted = count_words_in_list(
        get_words_only_small_letters(SaveRead.read_txt_file_to_string(base_path)))
    reference_words_counted = count_words_in_list(
        get_words_only_small_letters(SaveRead.read_txt_file_to_string(reference_path)))
    # Get the ratio of base words count relative to reference words count.
    base_words_relative_reference_count_tuple_list = get_ratio_of_base_words_count_relative_to_reference_words_count(
        base_words_counted, reference_words_counted)
    # Sort the relative count of base words
    sorted_base_words_relative_reference_count_tuple_list = sort_words_count(
        base_words_relative_reference_count_tuple_list)
    most_meaningful_words = get_only_common_words(
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
