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




def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

#print(f'Количество попыток: {random_predict()}')