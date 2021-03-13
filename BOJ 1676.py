n = int(input())

countTwo = 0
countFive = 0
 
for i in range(1, n+1):
    if not i%2:
        k = i
        while not k%2:
            countTwo += 1
            k /= 2
          
    if not i%5:
        k = i
        while not k%5:
            countFive += 1
            k /= 5
 
print(min(countTwo, countFive))