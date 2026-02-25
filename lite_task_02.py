n = int(input("Введите кол-во белочек: "))
k = int(input("Введите кол-во орешков: "))

res = 0

if n > 10000 or k > 10000:
    print("Нелья по заданию!")

else:
    res = k%n
    print(res)
