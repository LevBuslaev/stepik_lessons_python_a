n = int(input())
while n != 0:
    n1 = n % 10
    n = n // 10
    n2 = n % 10
    print(n1)
    print(n2)
    #if n1 < n2:

#=====================================
'''Упорядоченные цифры 🌶️
Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести «YES» если последовательность его цифр при просмотре справа налево является упорядоченной по неубыванию и «NO» в противном случае.

Тестовые данные 🟢
Sample Input 1:

5321
Sample Output 1:

YES
Sample Input 2:

7820
Sample Output 2:

NO'''