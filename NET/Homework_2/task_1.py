'''
Задача №1
Ипотечный калькулятор. В новом банке решили начать выдавать ипотеку. Появилась необходимость разработать для них ипотечный калькулятор. Нужно рассчитать финальную процентную ставку по ипотеке. От каких критериев зависит скидка на ипотеку:

Если клиент из Дальнего Востока (список субъектов, входящих в регион, определить самостоятельно), то базовая ставка становится 2%.
Если количество детей больше 3, то базовая ставка уменьшается на 1%.
Если у клиента зарплатный проект в этом банке, то базовая ставка уменьшается на 0.5%.
Если в этом же банке будет оформлена страхование, то базовая ставка уменьшается на 1.5% Базовую процентную ставку выбрать самостоятельно. Если клиент оформляет ипотеку по дальневосточной программе, то остальные скидки не применяются.
'''

client_place = input('Введите место жительства клиента: ')
number_of_children = int(input('Введите целое число, обозначающее количество детей клиента: '))
salary_card = input('Является ли клиент держателем зарплатной карты этого банка (да/нет): ')
insurance = input('Будет ли клиент оформлять страхование в этом банке (да/нет): ')

if client_place == 'Дальний Восток': 
    print("Базовая ставка для клиента составляет: 2.0 процента")

if client_place == 'Москва' or 'Московская область' or 'Республика Адыгея' or 'Санкт-Петербург' or 'Казань': 
    base_rate = 6

    if number_of_children >= 3:
        discount_number_of_children = 1
    else:
        discount_number_of_children = 0

    if salary_card == 'да':
        discount_salary_card = 0.5
    else: 
        discount_salary_card = 0

    if insurance == 'да':
        discount_insurance = 1.5
    else: 
        discount_insurance = 0
    
    base_rate = base_rate - (discount_number_of_children + discount_salary_card + discount_insurance)
    print(f" Базовая ставка для клиента составляет:  {base_rate} процента(ов)")

else:
    print('УПС! В Вашем регионе банк пока не выдаёт ипотеку. Мы работаем над этим. Обратитесь, пожалуйста, позднее.')
  