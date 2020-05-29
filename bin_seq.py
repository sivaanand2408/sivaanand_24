N = int(input())
for i in range(1, N+1):
    print(bin(i).replace('0b', ''), end = ' ')
