import random


def  get_numbers_ticket(min, max, quantity):
#Умови виконання
    if min>=1 and max<=1000 and  quantity>=1 and  quantity<=1000 and quantity>=min and quantity<=max:
#Список чисел
     numbers = []
     #Діапазон чисел
     range1=range(min,max)
     #Вибір числа з діапазону
     number=random.sample(range1,k=quantity)
     #Додавання випадкового числа в список
     numbers.append(number)
    
     #Повернення cписку випадкових чисел
     return numbers
    else:
     #Повернення пустого списку якщо умови не виконані
     return[]

print(get_numbers_ticket(1,48,7))