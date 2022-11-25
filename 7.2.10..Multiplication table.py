# put your python code here
n = int(input())
for _ in range(1, 11):
    print(str(n) + ' x ' + str(_) + ' = ' + str(n * _))


'''Таблица умножения
Дано натуральное число nn. Напишите программу, которая выводит таблицу умножения на nn.

Формат входных данных
На вход программе подается натуральное число.

Формат выходных данных
Программа должна вывести таблицу умножения на введенное число.

Примечание. В качестве знака умножения используйте английскую букву x.

Тестовые данные 🟢
Sample Input 1:

5
Sample Output 1:

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
Sample Input 2:

9
Sample Output 2:

9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 90
Sample Input 3:

4
Sample Output 3:

4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40
Напишите программу. Тестируется через stdin → stdout
Верно решили 97 736 учащихся
Из всех попыток 64% верных
Time Limit: 15 секунд
Memory Limit: 256 MB

Python 3
# put your python code here
n = int(input())
for _ in range(1, 11):
    print(str(n) + ' x ' + str(_) + ' = ' + str(n * _)) 



1
# put your python code here
2
n = int(input())
3
for _ in range(1, 11):
4
    print(str(n) + ' x ' + str(_) + ' = ' + str(n * _)) 
5
​
6
​
7
​
8
​
9
​
10
​
Test input:
4
Test output:
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40

Максимум 5 баллов за решение.'''