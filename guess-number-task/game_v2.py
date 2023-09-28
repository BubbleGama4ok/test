"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

#number = np.random.randint(1, 101) # загадываем число

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
    return(count)

def game_core_v3(number: int = 1) -> int:
    """угадываем число по алгоритму

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    pr_min=1
    pr_max=101
    count = 0
    predict = np.random.randint(1, 101)#компьютер предсказывает число
    
    while number != predict: # пока загаданное число не равно предсказанному
        
        count += 1
        
        if predict > number:# если предсказанное число больше загаданного
            pr_max = predict
            predict = round((pr_min + pr_min)/2) 
        
        elif predict < number:# если число меньше загаданного
            pr_min = predict
            predict = round((pr_min + pr_max)/2)
    #print(f'число угадано ! Это число {number}, за {count} попыток.')
    return count  
#print(f'Количество попыток: {game_core_v3()}')


#print(f'Количество попыток: {random_predict()}')

def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем из 1000 подходов
    угадывает наш алгоритм

    Args:
        game_core_v3 (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = []#список для сохранения количества попыток
    np.random.seed(1)#фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size = (1000))
    #загадали список чисел
    
    for number in random_array:
        count_ls.append(game_core_v3(number))
        
    score = int(np.mean(count_ls))#находим среднее количество попыток
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

score_game(game_core_v3)