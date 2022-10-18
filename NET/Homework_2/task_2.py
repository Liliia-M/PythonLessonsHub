'''
Задание №2
Разработать приложение для определения знака зодиака по дате рождения.

Пример:

Введите месяц: март
Введите число: 6

Вывод:
Рыбы'''

month = input('Введите название месяца (январь, февраль, март и т.д.): ')
date = int(input('Введите дату (от 1 до 31): '))

if month == 'март' and 31 >= date >= 21 or month == 'апрель' and date <= 19:
  print('Овен')
elif month == 'апрель' and 30 >= date >= 20 or month == 'май' and date <= 20:
  print('Телец')  
elif month == 'май' and 31 >= date >= 21 or month == 'июнь' and date <= 21:
  print('Близнецы') 
elif month == 'июнь' and 30 >= date >= 22 or month == 'июль' and date <= 22:
  print('Рак') 
elif month == 'июль' and 31 >= date >= 23 or month == 'август' and date <= 22:
  print('Лев') 
elif month == 'август' and 31 >= date >= 23 or month == 'сентябрь' and date <= 22:
  print('Дева') 
elif month == 'сентябрь' and 30 >= date >= 23 or month == 'октябрь' and date <= 23:
  print('Весы') 
elif month == 'октябрь' and 31 >= date >= 24 or month == 'ноябрь' and date <= 22:
  print('Скорпион') 
elif month == 'ноябрь' and 30 >= date >= 23 or month == 'декабрь' and date <= 21:
  print('Стрелец') 
elif month == 'декабрь' and 31 >= date >= 22 or month == 'январь' and date <= 20:
  print('Козерог') 
elif month == 'январь' and 30 >= date >= 21 or month == 'февраль' and date <= 18:
  print('Водолей') 
elif month == 'февраль' and 29 >= date >= 19 or month == 'март' and date <= 20:
  print('Рыбы') 
else: 
  print('Проверьте правильность ввода даты и месяца')
