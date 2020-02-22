# This script contains the code from the interactive REPL examples from the first half of chapter 5


def calculate_mean(numbers: list) -> float:
    """
    Example function for purposes of explaining testing concepts
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# these pass
assert calculate_mean([]) == 0.0
assert calculate_mean([1, 2, 3, 4]) == 2.5
assert calculate_mean([1, 0, -1]) == 0.0
assert calculate_mean([0]) == 0.0

# this fails
assert calculate_mean([1000, 7000, 7000000]) == 1.0
