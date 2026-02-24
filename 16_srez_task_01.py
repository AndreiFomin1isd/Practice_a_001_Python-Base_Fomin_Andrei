word = input("Ввод: ")
s = str(word)
len = len(word)
for i in range(1//2):
    if s[i] != s[-1-i]:
        print("Не он")
else:
    print("Он")


