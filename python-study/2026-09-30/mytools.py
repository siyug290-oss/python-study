def calc_bmi(height, weight):
    return weight / height ** 2

def find_max(numbers):
    best = numbers[0]
    for n in numbers:
        if n > best:
            best = n
    return best