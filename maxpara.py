# -*- coding: utf-8 -*-
"""
136) (А.А. Богданов) Дана последовательность N целых 
положительных чисел, не превышающих 10000. Рассматриваются 
все пары элементов последовательности, сумма которых нечётна, 
а элементы пары находятся на расстоянии равном младшей цифре 
левого элемента пары. Левый элемент пары имеет меньший индекс, 
чем правый. Среди всех таких пар нужно найти и вывести пару 
с максимальной суммой элементов. Если одинаковую максимальную 
сумму имеет несколько пар, можно вывести любую из них. Если 
подходящих пар в последовательности нет, нужно вывести два нуля. 
2 <= N <= 10000.
Входные данные: 
В первой строке записано натуральное число N (2 <= N <= 10000) – 
количество чисел в последова-тельности. В следующих N cтроках 
записаны числа, входящие в последовательность, по одному в 
каждой строке.
Выходные данные: 
Программа должна вывести пар с максимальной суммой, 
удовлетворяющую условию задачи, или два нуля, если таких пар нет.
Пример входных данных: 
5 
11 
12 
12 
13 
15
Пример выходных данных для приведённого примера входных данных:
12 15
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/136.in")

n = int(input())

b = [0]*10

for i in range(min(n,10)):
  b[i] = int(input())
L, R = 0, 0

for i in range(n-1):
  q = b[0] % 10
  if b[q] > 0 and (b[0]+b[q]) % 2 !=0 and b[0]+b[q] > L+R:
    L, R = b[0], b[q]
  b.pop(0) # сдвиг буфера влево
  if i+10 <= n:
    b.append( int(input()) )
  else: 
    b.append( 0 )

print( L, R ) 

sys.stdin = save_stdin
