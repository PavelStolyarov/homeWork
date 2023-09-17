# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.


# кол-во кустов
n = int(input())
numberOfBerries = [int(input()) for i in range(n)]

max = 0
buf = 0

for i in range(n):
    if i == 0: max = numberOfBerries[n - 1] + numberOfBerries[0] + numberOfBerries[1] if max < (numberOfBerries[n - 1] + numberOfBerries[0] + numberOfBerries[1]) else max
    elif i == n - 1: max = numberOfBerries[n - 1] + numberOfBerries[n - 2] + numberOfBerries[0] if max < (numberOfBerries[n - 2] + numberOfBerries[n - 1] + numberOfBerries[0]) else max
    else:
        if max < numberOfBerries[i] + numberOfBerries[i - 1] + numberOfBerries[i + 1]:
            max = numberOfBerries[i] + numberOfBerries[i - 1] + numberOfBerries[i + 1]
print(max)    
