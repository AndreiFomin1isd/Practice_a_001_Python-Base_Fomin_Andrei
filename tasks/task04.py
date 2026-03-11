number = int(input("Сколько чисел?: "))

f = False

for i in range(number):
    num = int(input(f'''Введите число {i+1}: '''))
    if num > 50:
        print("Больше 50: ", num)
        f = True
        break
if not f:
    print("Не найдено: ")
    