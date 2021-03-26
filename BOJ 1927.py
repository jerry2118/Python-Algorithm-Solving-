import sys
import heapq
 
N = int(sys.stdin.readline().rstrip())
_list = []

for i in range(N):
    x = int(sys.stdin.readline().rstrip())

    if x > 0:
        heapq.heappush(_list, x)
    else:
        if not _list:
            print('0')
        else:
            print(heapq.heappop(_list))