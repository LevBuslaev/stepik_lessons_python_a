
# put your python code here
m = int(input())
n = int(input())
for _ in range(m, n + 1):
    if _ % 17 == 0 or _ % 10 == 9 or _ % 15 == 0:
        print(_)

""" https://www.youtube.com/watch?v=OGGUQiNI3OE&t=2294s     youtube. С 37 минуты """

"""    Последовательность чисел 4
Даны два натуральных числа mm и nn ( m \le nm≤n). Напишите программу, которая выводит все числа от mm до nn включительно удовлетворяющие хотя бы одному из условий:

число кратно 17;
число оканчивается на 9;
число кратно 3 и 5 одновременно.
Формат входных данных
На вход программе подаются два натуральных числа mm и nn (m \le nm≤n), каждое на отдельной строке.

Формат выходных данных
Программа должна вывести числа в соответствии с условием задачи.

Примечание. Если чисел удовлетворяющих условию нет, выводить ничего не надо.

Тестовые данные 🟢
Sample Input 1:

1
20
Sample Output 1:

9
15
17
19
Sample Input 2:

17
17
Sample Output 2:

17
Sample Input 3:

19
19
Sample Output 3:

19   """