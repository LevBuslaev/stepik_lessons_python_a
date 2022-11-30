# put your python code here
n = int(input())
sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum -= i
    else:
        sum += i
print(sum)

# ===========================================================================
'''7.3 Частые сценарии
10 из 16 шагов пройдено
33 из 83 баллов  получено
Знакочередующаяся сумма
На вход программе подается натуральное число nn. Напишите программу вычисления знакочередующей суммы 
1-2+3-4+5-6 + \ldots + (-1)^{n+1}n.
1−2+3−4+5−6+…+(−1) 
n+1
 n.

Входные данные
На вход программе подается натуральное число nn.

Выходные данные
Программа должна вывести единственное число в соответствии с условием задачи.

Тестовые данные 🟢
Sample Input 1:

1
Sample Output 1:

1
Sample Input 2:

5
Sample Output 2:

3
Sample Input 3:

3
Sample Output 3:

2
Напишите программу. Тестируется через stdin → stdout
Верно решил 88 261 учащийся
Из всех попыток 48% верных
 Абсолютно точно.
# put your python code here
n = int(input())
sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum -= i
    else:
        sum += i
print(sum)
1
# put your python code here
2
n = int(input())
3
sum = 0
4
for i in range(1, n + 1):
5
    if i % 2 == 0:
6
        sum -= i
7
    else:
8
        sum += i
9
print(sum)
10
​
11
​
12
​
13
​
14
​
Test input:
3
Test output:
2'''