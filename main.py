# ОБЩАЯ ЧАСТЬ
# #Контейнер расчета
# from sympy import *
# k, T, C, L = symbols('k T C L')

#1 способ - линейный (1-ый пункт задания)
# C_ost = 100000
# Am_lst = []
# C_ost_lst = []
# for i in range(5):
#   Am = (C - L) / T
#   C_ost -= Am.subs({C: 100000, T: 5, L: 0})
#   Am_lst.append(round(Am.subs({C: 100000, T: 5, L: 0}), 2))
#   C_ost_lst.append(round(C_ost, 2))
# print('Am_lst:', Am_lst)
# print('C_ost_lst:', C_ost_lst)

# #2 способ - уменьшаемый остаток (2-ой пункт задания)
# Aj = 0
# C_ost = 100000
# Am_lst_2 = []
# C_ost_lst_2 = []
# for i in range(5):
#   Am = k * 1 / T * (C - Aj)
#   C_ost -= Am.subs({C: 100000, T: 5, k: 2})
#   Am_lst_2.append(round(Am.subs({C: 100000, T:5, k:2}), 2))
#   Aj += Am
#   C_ost_lst_2.append(round(C_ost, 2))
# print('Am_lst_2:', Am_lst_2)
# print('C_ost_lst_2:', C_ost_lst_2)

# 3-ий пункт общего задания
# Контейнер расчета
from sympy import*
k, T, C, L = symbols('k T C L')

#1 способ - линейный способ
C_ost = 50000
Am_lst = []
C_ost_lst = []
for i in range(9):
    Am = (C - L) / T 
    C_ost -= Am.subs({C: 50000, T: 9, L: 0})
    Am_lst.append(round(Am.subs({C: 50000, T: 9, L: 0}), 2))
    C_ost_lst.append(round(C_ost, 2))
print('Am_lst:', Am_lst)
print('C_ost_lst:', C_ost_lst)

#2 способ - уменьшаемый остаток
Aj = 0
C_ost = 50000
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(9):
    Am = k * 1 / T * (C - Aj)
    C_ost -= Am.subs({C: 50000, T: 9, k: 2})
    Am_lst_2.append(round(Am.subs({C: 50000, T: 9, k: 2}), 2))
    Aj += Am
    C_ost_lst_2.append(round(C_ost, 2))
print('Am_lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)

#Контейнер для табличного вывода
import pandas as pd
from pandas.core.internals.managers import ensure_np_dtype
Y = range(1, 10)
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
plt.savefig('chart1.png') #диаграмма остаточной стоимости (линейный способ)
plt.figure()
plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label = 'Am_2')
plt.savefig('chart2.png') #диаграмма остаточной стоимости (уменьшаемый остаток)
vals = Am_lst
labels = [str(x) for x in range(1, 10)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1) #для круговых диаграмм
flig, ax = plt.subplots()
ax.pie(vals, labels = labels, autopct = '%1.1f%%', shadow=True, explode = explode, wedgeprops = {'lw':1, 'ls': '--', 'edgecolor': 'k'}, rotatelabels = True)
ax.axis('equal')
plt.savefig('chart3.png') #распределение амортизации по годам (линейный способ)
vals = Am_lst_2
labels = [str(x) for x in range(1, 10)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
flig, ax = plt.subplots()
ax.pie(vals, labels = labels, autopct = '%1.1f%%', shadow=True, explode = explode, wedgeprops = {'lw':1, 'ls': '--', 'edgecolor': 'k'}, rotatelabels = True)
ax.axis('equal')
plt.savefig('chart4.png') #распределение амортизации по годам (уменьшаемый остаток)

table1_am = list(zip(Y, Am_lst))
table2_am = list(zip(Y, Am_lst_2))
tfame_am = pd.DataFrame(table1_am, columns = ['Y', 'Am_lst'])
tfame2_am = pd.DataFrame(table2_am, columns = ['Y', 'Am_lst_2'])
plt.figure()
plt.bar(tfame_am['Y'], tfame_am['Am_lst']) #создание столбчатой диаграммы
plt.savefig('chart5.png') #амортизация по годам (линейный способ)
plt.figure()
plt.bar(tfame_am['Y'], tfame2_am['Am_lst_2'])
plt.savefig('chart6.png') #амортизация по годам (уменьшаемый остаток)
plt.figure()

# # ИНДИВИДУАЛЬНАЯ ЧАСТЬ
# # Контейнер расчета
from sympy import *

k, T, C, L = symbols("k C T L")
# 1 способ - линейный способ
C_ost = 120000
Am_lst = []
C_ost_lst = []
for i in range(10):
    Am = (C - L) / T
    C_ost -= Am.subs({C: 120000, T: 10, L: 0})
    Am_lst.append(round(Am.subs({C: 120000, T: 10, L: 0}), 2))
    C_ost_lst.append(round(C_ost, 2))
print("Am_lst:", Am_lst)
print("C_ost_lst:", C_ost_lst)

# 2 способ - уменьшаемый остаток
Aj = 0
C_ost = 120000
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(10):
    Am = k * 1 / T * (C - Aj)
    C_ost -= Am.subs({C: 120000, T: 10, k: 2})
    Am_lst_2.append(round(Am.subs({C: 120000, T: 10, k: 2}), 2))
    Aj += Am
    C_ost_lst_2.append(round(C_ost, 2))
print("Am_lst_2:", Am_lst_2)
print("C_ost_lst_2:", C_ost_lst_2)

# Контейнер для табличного вывода
import pandas as pd
from pandas.core.internals.managers import ensure_np_dtype

Y = range(1, 11)
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tfame = pd.DataFrame(table1, columns=(["Y", "C_ost_lst", "Am_lst"]))
tfame2 = pd.DataFrame(table2, columns=(["Y", "C_ost_lst_2", "Am_lst_2"]))
print("\n")
print(tfame)
print(tfame2)

# Контейнер визуализации
import numpy as np
import matplotlib.pyplot as plt

plt.plot(tfame["Y"], tfame["C_ost_lst"], label="Am")
plt.savefig("chart7.png")
plt.figure()
plt.plot(tfame2["Y"], tfame2["C_ost_lst_2"], label="Am_2")
plt.savefig("chart8.png")

vals = Am_lst
labels = [str(x) for x in range(1, 11)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
flig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    autopct="%1.1f%%",
    shadow=True,
    explode=explode,
    wedgeprops={"lw": 1, "ls": "-", "edgecolor": "k"},
    rotatelabels=True,
)
ax.axis("equal")
plt.savefig("chart9.png")

vals = Am_lst_2
labels = [str(x) for x in range(1, 11)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode,  wedgeprops={'lw':1, 'ls':'-', 'edgecolor':'k'}, rotatelabels = True )
ax.axis('equal')
plt.savefig('chart10.png')

table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tfame = pd.DataFrame(table1, columns = (['Y', 'Am_lst']))
tfame2 = pd.DataFrame(table2, columns = (['Y', 'Am_lst_2']))
plt.figure()
plt.bar(tfame['Y'], tfame['Am_lst'])
plt.savefig('chart11.png')
plt.figure()
plt.bar(tfame2['Y'], tfame2['Am_lst_2'])
plt.savefig('chart12.png')