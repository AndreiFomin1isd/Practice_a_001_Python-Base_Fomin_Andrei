N = int(input("Ввод: "))

count2 = 0
count3 = 0
count23 = 0

for i in range(1, N + 1):
    if i %2==0:
        count2+=1
    if i%3 == 0:
        count3+=1
    
    if i %2==0 and i %3==0:
        count23+=1

print(f'''
      на 2: {count2}  
      на 3: {count3}  
      на 2 и на 3: {count23}''')
    
