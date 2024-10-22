def generate_password(n):
    # проверяем чтобы число входи в диапозон
    if n < 3 or n > 20:
        return "Введите число от 3 до 20"

    list_ = ''

    for a in range(1, 21):  # Пары чисел подбираются от 1 до 20 для текущих чисел.
        for b in range(a + 1, 21):
            pair_sum = a + b  # Сумма пары
            if n % pair_sum == 0:  # Кратность суммы
                list_ += str(a) + str(b)

    return list_

human= input("Введите число от 3 до 20: ")  # Запрос ввода у человека

if human.isdigit():
    n = int(human)  # Вводим число
    if 3 <= n <= 20:  # Проверяем, что число в допустимом диапазоне
        result = generate_password(n)  #  пароль
        print("Сгенерированный пароль:", result) 
    else:
        print("Пожалуйста, введите корректное целое число.")
