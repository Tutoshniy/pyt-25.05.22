#Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")
count = 0
if len(str1) > len(str2):
    for i in range(len(str1)):
        if str1[i:(i+len(str2))] == str2[:len(str2)]:
            count+=1
else:
    for i in range(len(str2)):
        if str2[i:(i+len(str1))] == str1[:len(str1)]:
            count+=1
print(count)
