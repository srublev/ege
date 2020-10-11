# coding: utf-8

def get_numbers():
    number = int(input('Введите элемент последовательности (0 - завершение ввода) '))
    numbers = []
    while number != 0:
        numbers.append(number)
        number = int(input('Введите элемент последовательности (0 - завершение ввода) '))

    return numbers

def count_len_of_longest_progression(numbers):
    # Граничные случаи
    if len(numbers) < 2:
        return 0

    if len(numbers) == 2:
        return 2

    # Основной алгоритм
    max_len = 0
    curr_len = 2

    for i in range(1, len(numbers)-1):
        if (numbers[i-1] + numbers[i+1]) % 2 == 0 and (numbers[i-1] + numbers[i+1])/2 == numbers[i]:
            curr_len += 1
        else:
            if curr_len > max_len:
                max_len = curr_len
                curr_len = 2

    if curr_len > max_len:
        max_len = curr_len

    return max_len

if __name__ == '__main__':
    result = count_len_of_longest_progression(get_numbers())
    print('Количество чисел самой длинной прогрессии:', result)