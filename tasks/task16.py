stroka = str(input("Введите строку: "))

res = ""

for simvol in stroka:
    if not simvol.isdigit():
        res+=simvol
print("Строка без цифр: ", res)