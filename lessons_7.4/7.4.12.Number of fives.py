# put your python code here
n = int(input())
n_5 = 0
while n > 0 and n < 6:
    if n == 5:
        n_5 += 1
    n = int(input())
print(n_5)

# ===========================================
'''Количество
пятерок
На
вход
программе
подается
последовательность
целых
чисел
от
11
до
55, характеризующее
оценку
ученика, каждое
число
на
отдельной
строке.Концом
последовательности
является
любое
отрицательное
число, либо
число
большее
55.
Напишите
программу, которая
выводит
количество
пятерок.

Формат
входных
данных
На
вход
программе
подается
последовательность
чисел, каждое
число
на
отдельной
строке.

Формат
выходных
данных
Программа
должна
вывести
количество
пятерок.

Тестовые
данные 🟢
Sample
Input
1:

1
1
2
2
3
4
4
5
5
5
5
-17
1
2
5
4
Sample
Output
1:

4
Sample
Input
2:

5
5
-9
5
5
Sample
Output
2:

2
Sample
Input
3:

5
1
-5
4
5
3
-2
Sample
Output
3:

1
Напишите
программу.Тестируется
через
stdin → stdout
Верно
решили
85
577
учащихся
Из
всех
попыток
53 % верных
Time
Limit: 15
секунд
Memory
Limit: 256
MB

Python
3
n = int(input())
n_5 = 0
while n > 0 and n < 6 and n == 5:
    n_5 += 1
    n = int(input())
print(n_5)

1
# put your python code here
2
n = int(input())
3
n_5 = 0
4
while n > 0 and n < 6 and n == 5:
    5
n_5 += 1
6
n = int(input())
7
print(n_5)
8

9
​
10
​
11
​
12
​
Test
input:
1
1
2
2
3
4
4
5
5
5
5
-17
1
2
5
4
Test
output:
0     '''