stroka = str(input("Введите строку: "))
simvol = str(input("Введите символ: "))

index =- 1

for i in range(len(stroka)):
    if stroka[i] == simvol:
        index = i
        break

if index != -1:
    print("Индекс первого вхожденния: ", index)

else:
    print("Не найдено")