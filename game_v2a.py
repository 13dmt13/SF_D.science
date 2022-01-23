"""Угадай игру 2 Компьютер угадывает сам"""

from unicodedata import name
import numpy as np

def random_predict(number:int=1) -> int:
    """Случайно угадываем число.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count=0 # количество попыток
    begin=1 # начало интервала
    end=101 # конец интервала
    
    while count < 20: # Условие цикла
        count+=1 #Шаг цикла
        predict_number=np.random.randint(begin,end) # Предполагаемое число
        if number==predict_number:
            break # выход из цикла, если угадали 
    
        elif number<predict_number: # уменьшение интервала для поиска
            end=predict_number
            
        else: 
            
            number>predict_number # уменьшение интервала для поиска
            begin=predict_number
    
    return count # обнуление попыток
        
        
    
def score_game(random_predict) -> int:
    """Среднее количество попыток за 1000 подходов

    Args:
        random_predict ([type]): Функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    
    count_ls=[]# список сохранения попыток
    np.random.seed(1)# Фиксируем сид воспроизводимости
    random_array=np.random.randint(1,101, size=(1000))# загадываем список чисел 
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score=int(np.mean(count_ls))# нахождение среднего числа попыток
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)



if __name__=='__main__':
    #RUN
    score_game(random_predict)