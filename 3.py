#Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")
count = 0
if len(str2) > len(str1):
    temp = str2
    str2 = str1
    str1 = temp
print(str1, str2)
for i in range(len(str1)):
    if str1[i:(i+len(str2))] == str2[:len(str2)]:
        count+=1
print(count)
