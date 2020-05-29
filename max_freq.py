Num = int(input())
Arr = list(map(int, input().split()[:Num]))
max = 0
res = Arr[0] 
for i in Arr: 
    freq = Arr.count(i) 
    if freq > max: 
        max = freq 
        res = i
print(freq)
