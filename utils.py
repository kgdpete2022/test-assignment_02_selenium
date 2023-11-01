from typing import List


def are_equal_in_size(dimensions: List[tuple]):
    return len(set(dimensions)) == 1
