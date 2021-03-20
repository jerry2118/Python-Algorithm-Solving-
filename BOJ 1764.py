n, m = map(int, input().split())

ListN = []
ListM = []

for i in range(n):
    name = input()
    ListN.append(name)
    
for i in range(m):
    name = input()
    ListM.append(name)
    
answer = list(set(ListN)&set(ListM))

print(len(answer))

answer.sort()

for i in answer:
    print(i)