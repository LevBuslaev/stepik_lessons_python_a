# put your python code here
num_yes = 0

for i in range(1, 11):
    num = int(input())

    if num % 2 == 0:
        num_yes += 1
#  print(num_yes)

if num_yes == 10:
    print('YES')
else:
    print('NO')

'''Only even numbers 🌶️
Напишите программу, которая считывает последовательность из 10 целых чисел и определяет является ли каждое из них четным или нет.

Формат входных данных
На вход программе подаются 10 целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести строку «YES», если все числа четные и «NO» в ином случае.

Тестовые данные 🟢
Sample Input 1:

2
4
6
8
10
12
14
16
18
20
Sample Output 1:

YES
Sample Input 2:

1
2
3
4
5
6
7
8
9
10
Sample Output 2:

NO
Напишите программу. Тестируется через stdin → stdout
Верно решили 87 264 учащихся
Из всех попыток 50% верных
 Прекрасный ответ.
1
# put your python code here
2
num_yes = 0
3
​
4
for i in range (1, 11):
5
  num = int(input())
6

7
  if num % 2 == 0:
8
    num_yes += 1
9
#  print(num_yes)
10

11
if num_yes == 10:
12
  print('YES')
13
else:
14
  print('NO')
15
  '''