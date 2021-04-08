import sys


def makePi(str):
    pi = [0] * len(str)

    j = 0
    for i in range(1, len(str)):
        while j > 0 and str[j] != str[i]:
            j = pi[j-1]
        if str[j] == str[i]:
            j += 1
            pi[i] = j
    
    return pi

def kmp(str, P_str):
    pi = makePi(P_str)
    count = 0
    j = 0

    for i in range(0, len(str)):
        while j > 0 and str[i] != P_str[j]:
            j = pi[j-1]
        if str[i] == P_str[j]:
            if j == len(P_str)-1:
                count += 1
                j = pi[j]
            else:
                j += 1 
    return count

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

S = sys.stdin.readline().rstrip()

base = 'IO'

Pn = base * N + 'I'

ans = kmp(S, Pn)

print(ans)