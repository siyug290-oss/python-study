def calc_bmi(height,weight):
    return weight / height ** 2

print(calc_bmi(1.75,70))


def find_max(numbers):
    best = numbers[0]
    for n in numbers:
        if n > best:
            best = n
    return best

print(find_max([3,8,2,9,5]))