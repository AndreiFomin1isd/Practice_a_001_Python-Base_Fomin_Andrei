def IsPointInSquare(x,y):
    return abs(x) <= 1 and abs(y) <= 1

x = float(input("Введите X: "))
y = float(input("Введите Y: "))

if IsPointInSquare(x,y):
    print("Попадает")
else:
    print("Не попадает")