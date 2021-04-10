import sys

def find_all(num, _lst, target):
    count = 0

    for i in range(1, 1<<num):
        sum = 0

        for j in range(0, num):
            if i & (1 << j):
                sum += _lst[j]

        if sum == target:
            count += 1

    return count
    
N, S = map(int, sys.stdin.readline().rstrip().split())
_list = list(map(int, sys.stdin.readline().rstrip().split()))

answer = find_all(N, _list, S)

print(answer)
  