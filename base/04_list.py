numbers = list(map(int,["1","2","3"]))
print(numbers)

spisok = list(map(float,["0.4","0.1","1.64","8.6473"]))
print(spisok)

x = list("hello")
print(x)

spisok_1 = list("Добрый")
spisok_2 = list("день")
summa = spisok_1 + spisok_2
print(summa)

a = 5
b = '5'
#c = a+b
print(type(a))
print(type(b))

new_a = int(a)
new_b = int(b)

result = new_a + new_b
print(result)

new_a = list(str(a))
new_b = list(str(b))

result = new_a + new_b
print(result)