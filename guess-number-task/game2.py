import numpy as np
number = np.random.randint(1, 101) # загадываем число



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
    
    while number != predict: # пока загаданное число не равно предсказанному
        if (pr_max - pr_min) < 2:
            break
        count += 1
        
        if predict > number:# если предсказанное число больше загаданного
            pr_max = predict
            predict = round((pr_min + pr_min)/2) 
        
        elif predict < number:# если число меньше загаданного
            pr_min = predict
            predict = round((pr_min + pr_max)/2)
    #print(f'число угадано ! Это число {number}, за {count} попыток.')
    return count  
print(f'Количество попыток: {game_core_v3()}')




def score_game(game_core_v3) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)
    