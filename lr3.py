# import os
# my_secret = os.environ['GOOGLE_API_KEY']
# print(my_secret)

#ЛАБОРАТОРНАЯ РАБОТА №3
# 1 Задание - вместе с Максимовой Е.А.
# Cсылка на ремикс:https://replit.com/@9063191297/ZadaniieSonia
import os
my_secret = os.environ['SECRET_VATUTINA']
print(my_secret)
my_secret = os.environ['VATUTINA_SA_2']
print(my_secret)
my_secret = os.environ['VATUTINAS_SECRET_3']
print(my_secret)

# 2 задание (Вариант 6) - вместе с Мурзагалиевой Э.А
# Ссылка на ремикс: https://replit.com/@elmiramurzagali/LR2VatutinaKP2317#lr3.py
# Контейнер расчета
from sympy import*
k, T, C, L = symbols('k T C L')

#1 способ - линейный способ
C_ost = 15000 #согласно данным варианта 6 изменена начальная стоимость/Мурзагалиева Э.А.
Am_lst = []
C_ost_lst = []
for i in range(8): #изменен срок полезного использования на 8 лет/Мурзагалиева Э.А.
    Am = (C - L) / T 
    C_ost -= Am.subs({C: 15000, T: 8, L: 0}) #измененны вводные данные/Мурзагалиева Э.А.
    Am_lst.append(round(Am.subs({C: 15000, T: 8, L: 0}), 2)) #измененны вводные данные/Мурзагалиева Э.А.
    C_ost_lst.append(round(C_ost, 2))
print('Am_lst:', Am_lst)
print('C_ost_lst:', C_ost_lst)

#2 способ - уменьшаемый остаток
Aj = 0
C_ost = 15000 #согласно данным варианта 6 изменена начальная стоимость/Мурзагалиева Э.А
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(8): #изменен срок полезного использования на 8 лет/Мурзагалиева Э.А.
    Am = k * 1 / T * (C - Aj)
    C_ost -= Am.subs({C: 15000, T: 8, k: 2}) #измененны вводные данные/Мурзагалиева Э.А.
    Am_lst_2.append(round(Am.subs({C: 15000, T: 8, k: 2}), 2)) #измененны вводные данные/Мурзагалиева Э.А.
    Aj += Am
    C_ost_lst_2.append(round(C_ost, 2))
print('Am_lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)

#Контейнер для табличного вывода
import pandas as pd
from pandas.core.internals.managers import ensure_np_dtype
Y = range(1, 9) #изменен срок полезного использования на 8 лет/Мурзагалиева Э.А.
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tfame = pd.DataFrame(table1, columns = (['Y', 'C_ost_lst', 'Am_lst']))
tfame2 = pd.DataFrame(table2, columns = (['Y', 'C_ost_lst_2', 'Am_lst_2']))
print(tfame)
print(tfame2)

#Контейнер визуализации
import numpy as np
import matplotlib.pyplot as plt
plt.plot(tfame['Y'], tfame['C_ost_lst'], label = 'Am')
plt.savefig('chart13.png') #диаграмма остаточной стоимости (линейный способ)
plt.figure()
plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label = 'Am_2')
plt.savefig('chart14.png') #диаграмма остаточной стоимости (уменьшаемый остаток)
vals = Am_lst
labels = [str(x) for x in range(1, 9)] #изменен срок полезного использования на 8 лет/Мурзагалиева Э.А.
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1) #изменено на 8 значений тк СПИ 8 лет/Мурзагалиева Э.А.
flig, ax = plt.subplots()
ax.pie(vals, labels = labels, autopct = '%1.1f%%', shadow=True, explode = explode, wedgeprops = {'lw':1, 'ls': '--', 'edgecolor': 'k'}, rotatelabels = True)
ax.axis('equal')
plt.savefig('chart15.png') #распределение амортизации по годам (линейный способ)
vals = Am_lst_2
labels = [str(x) for x in range(1, 9)]  #изменен срок полезного использования на 8 лет/Мурзагалиева Э.А.
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1) #изменено на 8 значений тк СПИ 8 лет/Мурзагалиева Э.А.
flig, ax = plt.subplots()
ax.pie(vals, labels = labels, autopct = '%1.1f%%', shadow=True, explode = explode, wedgeprops = {'lw':1, 'ls': '--', 'edgecolor': 'k'}, rotatelabels = True)
ax.axis('equal')
plt.savefig('chart16.png') #распределение амортизации по годам (уменьшаемый остаток)

table1_am = list(zip(Y, Am_lst))
table2_am = list(zip(Y, Am_lst_2))
tfame_am = pd.DataFrame(table1_am, columns = ['Y', 'Am_lst'])
tfame2_am = pd.DataFrame(table2_am, columns = ['Y', 'Am_lst_2'])
plt.figure()
plt.bar(tfame_am['Y'], tfame_am['Am_lst']) #создание столбчатой диаграммы
plt.savefig('chart17.png') #амортизация по годам (линейный способ)
plt.figure()
plt.bar(tfame_am['Y'], tfame2_am['Am_lst_2'])
plt.savefig('chart18.png') #амортизация по годам (уменьшаемый остаток)
plt.figure()

#изменения нового варианта внесены корректно, вывод результатов корректный, в моей ЛР2 тоже был вариант 6, все диаграммы совпадают с моими в ЛР2/Мурзагалиева Э.А.
#оценка внесенных изменений: 5 баллов

# 4 задание - вместе с Третьяковым М.В.
# Ссылка на ремикс: https://replit.com/@adeptusmaxx/LR2VatutinaKP2317#main.py
# Контейнер расчета
from sympy import*
k, T, C, L = symbols('k T C L')

#1 способ - линейный способ
C_ost = 30000
Am_lst = []
C_ost_lst = []
for i in range(8): #Что это значит? (Ответ: Цикл выполняется 8(для каждого года эксплуатации от 1 до 8). i-счетчик итераций)
    Am = (C - L) / T 
    C_ost -= Am.subs({C: 30000, T: 8, L: 0})
    Am_lst.append(round(Am.subs({C: 30000, T: 8, L: 0}), 2))
    C_ost_lst.append(round(C_ost, 2))
print('Am_lst:', Am_lst)
print('C_ost_lst:', C_ost_lst)

#2 способ - уменьшаемый остаток
Aj = 0
C_ost = 30000
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(8):
    Am = k * 1 / T * (C - Aj)
    C_ost -= Am.subs({C: 30000, T: 8, k: 2})
    Am_lst_2.append(round(Am.subs({C: 30000, T: 8, k: 2}), 2))
    Aj += Am
    C_ost_lst_2.append(round(C_ost, 2))
print('Am_lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)

#Контейнер для табличного вывода
import pandas as pd #Что это значит? (Ответ: Импортируется библиотека pandas для работы с табличными данными)
from pandas.core.internals.managers import ensure_np_dtype
Y = range(1, 9) 
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tfame = pd.DataFrame(table1, columns = (['Y', 'C_ost_lst', 'Am_lst']))
tfame2 = pd.DataFrame(table2, columns = (['Y', 'C_ost_lst_2', 'Am_lst_2']))
print(tfame)
print(tfame2)

удаляю контейнер визуализации для пункта 3 общей части лр3