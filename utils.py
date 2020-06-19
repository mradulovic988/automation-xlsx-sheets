def find_max():
    numbers = [10, 22, 3, 15, 6, 2]

    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max


def test():
    pass