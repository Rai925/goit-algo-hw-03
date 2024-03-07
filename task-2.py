import random

# def get_user_numbers(min_num, max_num, quantity):
#     user_numbers = set()

#     while len(user_numbers) < quantity:
#         try:
#             user_input = int(input(f"Введіть число між {min_num} і {max_num}: "))
#             if min_num <= user_input <= max_num:
#                 user_numbers.add(user_input)
#             else:
#                 print(f"Будь ласка, введіть число в межах від {min_num} до {max_num}.")
#         except ValueError:
#             print("Будь ласка, введіть коректне ціле число.")

#     return sorted(list(user_numbers))

# def get_numbers_ticket(min_num, max_num, quantity):
#     if not (1 <= min_num <= max_num <= 1000 and 1 <= quantity <= max_num - min_num + 1):
#         return []

#     numbers_set = set()

#     while len(numbers_set) < quantity:
#         random_number = random.randint(min_num, max_num)
#         numbers_set.add(random_number)

#     return sorted(list(numbers_set))

# def check_results(user_numbers, result_numbers):
#     common_numbers = set(user_numbers).intersection(result_numbers)
#     return common_numbers

# min_value = 1
# max_value = 49
# quantity_value = 6

# user_numbers = get_user_numbers(min_value, max_value, quantity_value)
# result_numbers = get_numbers_ticket(min_value, max_value, quantity_value)

# print(f"Ваші обрані числа: {user_numbers}")
# print(f"Ваші унікальні випадкові числа: {result_numbers}")

# common_numbers = check_results(user_numbers, result_numbers)

# if common_numbers:
#     print(f"Спільні числа: {common_numbers}")
# else:
#     print("Спільних чисел немає.")

# print(f"Кількість спільних чисел: {len(common_numbers)}")

min_value = 1
max_value = 49
quantity_value = 6

user_numbers = sorted({int(input(f"Введіть число між {min_value} і {max_value}: ")) for _ in range(quantity_value)})
result_numbers = sorted(random.sample(range(min_value, max_value + 1), quantity_value))
common_numbers = sorted(set(user_numbers).intersection(result_numbers))

print(f"Ваші обрані числа: {user_numbers}")
print(f"Ваші унікальні випадкові числа: {result_numbers}")
print(f"Спільні числа: {common_numbers}" if common_numbers else "Спільних чисел немає.")
print(f"Кількість спільних чисел: {len(common_numbers)}")
