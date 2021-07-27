from task_7_1 import *
while True:
    n = (int(input('''Выберите вариант перевода:
    1. Дюймы в сантиметры
    2. Сантиметры в дюймы
    3. Мили в километры
    4. Километры в мили
    5. Фунты в килограммы
    6. Килограммы в фунты
    7. Унции в граммы
    8. Граммы в унции
    9. Галлон в литры
    10. Литры в галлоны
    11. Пинты в литры
    12. Литры в пинты  
    ''')))
    if n == 0:
        break
    num = int(input('Введите численное значение '))
    if n == 1:
        print(inch_centim(num), 'сантиметров')
    elif n == 2:
        print(centim_inch(num), 'дюймов')
    elif n == 3:
        print(mile_kilo(num), 'километров')
    elif n == 4:
        print(kilo_mile(num), 'миль')
    elif n == 5:
        print(pound_kg(num), 'килограмм')
    elif n == 6:
        print(kg_pound(num), 'фунт')
    elif n == 7:
        print(ounces_g(num), 'грамм')
    elif n == 8:
        print(g_ounces(num), 'унций')
    elif n == 9:
        print(gallon_litr(num), 'литров')
    elif n == 10:
        print(litr_gallon(num), 'галонн')
    elif n == 11:
        print(pints_litr(num), 'литров')
    elif n == 12:
        print(litr_pints(num), 'пинт')