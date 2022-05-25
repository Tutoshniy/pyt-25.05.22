#Подсчитать сумму цифр в вещественном числе.
chislo = int(input("Введите число: "))
sum = 0
while chislo != 0:
    sum+=chislo%10
    chislo//=10
print(sum)