s, e = input().split()
s = int(s)
e = int(e)
for numb in range(s+1,e):
	if numb % 2 == 0:
		print(numb, end =' ')
