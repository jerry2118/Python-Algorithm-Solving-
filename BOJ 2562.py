_list = []
_ind = [0]*300

for i in range(9):
    num = int(input())
    _list.append(num)
    _ind[num] = i

_list.sort()

print(_list[-1])
print(_ind[_list[-1]]+1)




