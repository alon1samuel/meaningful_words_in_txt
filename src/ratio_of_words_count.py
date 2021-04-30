from src.config import config


def turn_words_count_tuple_list_to_words_only(frequencies_list):
    return [x[config.WORDS_PLACE_IN_WORDS_COUNT_LIST] for x in frequencies_list]


def add_missing_base_words_to_reference_words_count(base_words, reference_words, reference_frequencies):
    base_words_not_in_ref = set(base_words) ^ set(reference_words)
    reference_counted_words_and_base_words = reference_frequencies + \
        [(x, config.DEFAULT_COUNT_WHEN_WORD_IS_NON_EXISTING) for x in base_words_not_in_ref]
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
    base_relative_to_reference_count = [base_words_count_tuple_list[x][config.COUNT_PLACE_IN_WORDS_COUNT_LIST] /
                                        base_words_with_reference_count[x][config.COUNT_PLACE_IN_WORDS_COUNT_LIST]
                                        for x in range_base_words]
    # Create a words_ count tuple list
    base_words_relative_reference_count_tuple_list = [
        (base_words_count_tuple_list[x][config.WORDS_PLACE_IN_WORDS_COUNT_LIST], 
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
