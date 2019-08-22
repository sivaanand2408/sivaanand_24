s, e = input().split()
s = int(s)
e = int(e)
for numb in range(s+1,e):
	if numb > 1:
		for i in range(2,numb):
			if numb % i == 0:
				break
		else:
			print(numb, end = ' ')
