import random

def generate_password(n):
    if n < 3 or n > 20:
        return []

    list_ = []  # список

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pair_sum = i + j
            if n % pair_sum == 0:
                list_.append(str(i) + str(j))

    result = ''.join(list_)
    return result

random_number = random.randint(3, 20)
password = generate_password(random_number)
print(f"Число на первой каменной вставке: {random_number} - Пароль: {password}")
