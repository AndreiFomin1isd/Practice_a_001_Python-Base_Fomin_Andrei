number = int(input("Введите число N: "))

chet_count = 0
nechet_count = 0

for i in range(1, number + 1):
    if i%2==0:
        chet_count+=1
    else:
        nechet_count+=1

print("Кол-во четных чисел: ", chet_count)
print("Кол-во нечетных чисел: ", nechet_count)