"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count

def game_core_v2(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем или увелииваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)
    
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count

def game_core_v3(number: int = 1) -> int:
    """угадываем число пока хз как

    Args:
        number (int, optional): _description_. Defaults to 1.

    Returns:
        int: _description_
    """
    pr_min=1
    pr_max=101
    count = 1
    predict = np.random.randint(1, 101)#компьютер предсказывает число
    
    while number != predict:# пока загаданное число не равно предсказанному
        count += 1
        if number > predict:# если предсказанное число меньше загаданного
            pr_min = predict
            predict = round((pr_min + pr_min)/2) 
        elif number < predict:# если число меньше загаданного
            pr_max = predict
            predict = round((pr_min + pr_max)/2)
    print(f'число угадано ! Это число {number}, за {count} попыток.')
    return count   


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    print('Run benchmarking for random_predict: ', end='')
    score_game(random_predict)

    print('Run benchmarking for game_core_v2: ', end='')
    score_game(game_core_v2)
    
    print('Run benchmarking for game_core_v3: ', end='')
    score_game(game_core_v3)