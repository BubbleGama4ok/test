import numpy as np

number = np.random.randint(1, 101) # загадываем число3

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