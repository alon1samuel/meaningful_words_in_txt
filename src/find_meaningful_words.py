import re
from collections import Counter
#
WORDS_PLACE_IN_FREQUENCY_LIST = 0
FREQUENCY_PLACE_IN_FREQUENCY_LIST = 1

# TODO: Add documentation to each function.
# TODO: Add tests to each function
# TODO: Divide function into different files.
# TODO: Add configuration file for magic numbers and strings.


def read_file(file_path: str) -> str:
    """Read file holding a string.

    Args:
        file_path (str)

    Returns:
        str: data in string format
    """
    with open(file_path, "r") as f:
        file_string = f.read()
    return file_string


def get_words_only_in_string(file_string: str) -> list:
    list_just_words = re.findall(r'\w+', file_string)
    list_words_small_letters = [x.lower() for x in list_just_words]

    return list_words_small_letters


def get_words_in_file(file_path):
    file_string = read_file(file_path)
    only_words_list = get_words_only_in_string(file_string)
    return len(only_words_list)


def sort_frequencies_list(frequencies_list):
    sorted_frequencies = sorted(
        frequencies_list, key=lambda x: x[1], reverse=True)
    return sorted_frequencies


def count_words_in_list(words_list):
    words_counter = dict(Counter(words_list))
    counted_words = sort_frequencies_list(words_counter.items())
    return counted_words


def get_only_common_words(words_frequencies_dict, number_of_most_common):
    return [x[WORDS_PLACE_IN_FREQUENCY_LIST] for x in words_frequencies_dict[:number_of_most_common]]


def get_most_common_words_in_play(file_path, number_of_most_common):

    file_string = read_file(file_path)
    only_words_list = get_words_only_in_string(file_string)
    words_frequencies_dict = count_words_in_list(only_words_list)
    most_common_words = get_only_common_words(
        words_frequencies_dict, number_of_most_common)
    return most_common_words


def turn_frequencies_into_words(frequencies_list):
    return [x[0] for x in frequencies_list]


def create_whole_frequencies_list(base_words, reference_words, reference_frequencies):
    base_words_not_in_ref = set(base_words) ^ set(reference_words)
    ref_freq_added_base_words = reference_frequencies + \
        [(x, 1) for x in base_words_not_in_ref]
    ref_words_whole = turn_frequencies_into_words(ref_freq_added_base_words)
    return ref_words_whole, ref_freq_added_base_words


def calculate_relative_from_frequencies(base_words, base_freq, ref_words_whole, ref_freq_added_base_words):

    ref_ind = [ref_words_whole.index(x) for x in base_words]
    base_relative = [(x[WORDS_PLACE_IN_FREQUENCY_LIST], x[FREQUENCY_PLACE_IN_FREQUENCY_LIST] /
                      ref_freq_added_base_words[ref_ind[ind]][FREQUENCY_PLACE_IN_FREQUENCY_LIST])
                     for ind, x in enumerate(base_freq)]
    return base_relative


def get_relative_frequencies(base_freq, ref_freq):
    base_words = turn_frequencies_into_words(base_freq)
    ref_words = turn_frequencies_into_words(ref_freq)
    ref_words_whole, ref_freq_added_base_words = create_whole_frequencies_list(
        base_words, ref_words, ref_freq)
    base_relative = calculate_relative_from_frequencies(
        base_words, base_freq, ref_words_whole, ref_freq_added_base_words)

    return base_relative
    pass


def find_meaningful_words_in_file_from_other(base_path, referance_path, number_of_words):
    base_words_frequencies = count_words_in_list(
        get_words_only_in_string(read_file(base_path)))
    referance_words_frequencies = count_words_in_list(
        get_words_only_in_string(read_file(referance_path)))
    base_relative_frequencies = get_relative_frequencies(
        base_words_frequencies, referance_words_frequencies)
    base_relative_frequencies = sort_frequencies_list(
        base_relative_frequencies)
    most_meaningful_words = get_only_common_words(
        base_relative_frequencies, number_of_words)
    return most_meaningful_words


def main(print_results=True):
    hamlet_path = "hamlet.txt"
    # Find how many words are there in hamlet txt file.
    hamlet_words_number = get_words_in_file(hamlet_path)
    if print_results:
        print(f"There are {hamlet_words_number} words in hamlet plat.")

    # Find the 30 most common words.
    how_many_common_words = 30
    hamlet_most_common_words = get_most_common_words_in_play(
        hamlet_path, how_many_common_words)
    if print_results:
        print(
            f"The {how_many_common_words} most common words in hamlet are - {hamlet_most_common_words}")

    # Having macbeth txt, could you find the most meaningful words in the hamlet file.
    macbeth_path = "macbeth.txt"
    hamlet_meaningful_words = find_meaningful_words_in_file_from_other(
        hamlet_path, macbeth_path, how_many_common_words)
    if print_results:
        print(
            f"These are the most meaningful words in the hamlet play: {hamlet_meaningful_words}")

    return hamlet_words_number, hamlet_most_common_words, hamlet_meaningful_words


if __name__ == "__main__":
    main()
