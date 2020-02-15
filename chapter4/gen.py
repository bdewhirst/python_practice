# Chapter 4 exercise to create a small generator


def squarer(vals: list) -> None:
    """
    given a list of numbers, calculate the square of each one
    """
    for val in vals:
        yield val ** 2


squarer([1, 2, 3])
squarer(range(100_000_000))  # generators can be passed other generators-- range is a generator
