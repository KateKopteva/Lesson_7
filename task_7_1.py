# 1. Дюймы в сантиметры
def inch_centim(num):
    conv_ratio1 = 2.54
    cm = num * conv_ratio1
    return cm
# 2. Сантиметры в дюймы
def centim_inch(num):
    conv_ratio2 = 0.393701
    inch = num * conv_ratio2
    return inch
# 3. Мили в километры
def mile_kilo(num):
    conv_ratio3 = 1.61
    km = num * conv_ratio3
    return km
# 4. Километры в мили
def kilo_mile(num):
    conv_ratio4 = 0.621371
    mile = num * conv_ratio4
    return mile
# 5. Фунты в килограммы
def pound_kg(num):
    conv_ratio5 = 0.4536
    kg = num * conv_ratio5
    return kg
# 6. Килограммы в фунты
def kg_pound(num):
    conv_ratio6 = 2.2046
    pound = num * conv_ratio6
    return pound
# 7. Унции в граммы
def ounces_g(num):
    conv_ratio7 = 28,3495
    g = num * conv_ratio7
    return g
# 8. Граммы в унции
def g_ounces(num):
    conv_ratio8 = 0.0353
    ounces = num * conv_ratio8
    return ounces
# 9. Галлон в литры
def gallon_litr(num):
    conv_ratio9 = 4.5461
    litr = num * conv_ratio9
    return litr
# 10. Литры в галлоны
def litr_gallon(num):
    conv_ratio10 = 0.22
    gallon = num * conv_ratio10
    return gallon
# 11. Пинты в литры
def pints_litr(num):
    conv_ratio11 = 0.5683
    litr = num * conv_ratio11
    return litr
# 12. Литры в пинты
def litr_pints(num):
    conv_ratio12 = 1.7598
    pints = num * conv_ratio12
    return pints