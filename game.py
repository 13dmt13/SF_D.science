"""Угадай число"""

import numpy as np

number=np.random.randint(1,101) #zagadivaem chislo

#kol-vo try
count=0

while True:
    count+=1
    predict_number=int(input('Ugadai chislo ot 1 do 100 - '))
    
    if predict_number > number:
        print('Chislo menshe')
        
    elif predict_number < number:
        print('Chislo bolshe')
        
    else:
        print(f'YES! YOU WIN! THIS NUMBER={number}, YOUR COUNTS={count}')
        break #END GAME     
           