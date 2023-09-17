# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input())
m = int(input())
nList = [int(input()) for i in range(n)]
mList = [int(input()) for i in range(m)]

nSet = set(sorted(nList))
mSet = set(sorted(mList))


print(nSet & mSet)

