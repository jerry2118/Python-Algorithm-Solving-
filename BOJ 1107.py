import sys

channel = int(sys.stdin.readline().rstrip())

n = int(sys.stdin.readline().rstrip())

if n == 0:
    if channel <= 97 or channel >= 104:
        print(len(str(channel)))
        sys.exit()
    else:
        print(abs(channel - 100))
        sys.exit()
if n == 10:
    print(abs(channel - 100))
    sys.exit()
x = list(map(int, sys.stdin.readline().rstrip().split()))

excList = [0]*15

curChannel = 100
cnt = 0
answer = 0

blocked = True

for i in range(len(x)):
    excList[x[i]] = 1

for i in range(1, 10):
    if not excList[i]:
        blocked = False

if blocked:
    print(min(channel + 1, abs(channel - 100)))
    sys.exit()
    
def check(lis):
    global excList
    
    for i in lis:
        if excList[i]:
            return False
    
    return True

def getMin(num):
    global channel 
    global curChannel
    
    x = list(map(int, list(str(num))))
    k = num
    
    while not check(x):
        k += 1
        x = list(map(int, list(str(k))))
    maximum = k
    
    k = num
    x = list(map(int, list(str(k))))
    
    while not check(x):
        k -= 1
        
        if k < 0:
            k = 99999999999
            break
        x = list(map(int, list(str(k))))
        
    minimum = k
    
    if(abs(channel - maximum) <= abs(channel - minimum)):
        if abs(channel - maximum) == abs(channel - minimum):
            if len(str(maximum)) <= len(str(minimum)):
                curChannel = maximum
            else:
                curChannel = minimum
        else:        
            curChannel = maximum
    else:
        curChannel = minimum

if curChannel == channel:
    print(0)
    sys.exit()
elif 97 <= channel and 104 >= channel:
    print(abs(channel-100))
    sys.exit()
else:
    getMin(channel)
    cnt += len(str(curChannel))
    cnt += abs(channel - curChannel)
    answer = min(abs(channel - 100), cnt)
    
    print(answer)
    sys.exit()