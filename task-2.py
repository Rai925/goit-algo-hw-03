import random

def get_numbers_ticket(min_num, max_num, quantity):
    if not (1 <= min_num <= max_num <= 1000 and 1 <= quantity <= max_num - min_num + 1):
        return []

    numbers_set = set()

    while len(numbers_set) < quantity:
        random_number = random.randint(min_num, max_num)
        numbers_set.add(random_number)

    return sorted(list(numbers_set))

min_value = 1
max_value = 49
quantity_value = 6
result_numbers = get_numbers_ticket(min_value, max_value, quantity_value)
print(f"Ваші унікальні випадкові числа: {result_numbers}")