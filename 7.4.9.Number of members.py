# put your python code here
sum = 0
word = input()
while word != 'стоп' and word != 'хватит' and word != 'достаточно':
    sum += 1
    word = input()
print(sum)




'''Количество членов
На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности является одно из трех слов: «стоп», «хватит», «достаточно» (маленькими буквами, без кавычек). Напишите программу, которая выводит общее количество членов данной последовательности.

Формат входных данных
На вход программе подается последовательность слов, каждое слово на отдельной строке.

Формат выходных данных
Программа должна вывести общее количество членов данной последовательности.

Тестовые данные 🟢
Sample Input 1:

Skyrim
GTA
Mafia
стоп
Battlefield
Sample Output 1:

3
Sample Input 2:

Yandex
Google
Opera
Safari
хватит
Mozilla
Sample Output 2:

4
Sample Input 3:

Skype
Viber
Telegram
WhatsApp
Discord
достаточно
Sample Output 3:

5
Напишите программу. Тестируется через stdin → stdout
Верно решили 86 805 учащихся
Из всех попыток 58% верных
Time Limit: 15 секунд
Memory Limit: 256 MB

Python 3
1
# put your python code here
2
sum = 0
3
word = input()
4
while word != 'стоп' and word != 'хватит' and word != 'достаточно':
5
    sum += 1
6
    word = input()
7
print(sum)
8
​
9
​
10
​
11
​
Test input:
Skype
Viber
Telegram
WhatsApp
Discord
достаточно
Test output:
5'''