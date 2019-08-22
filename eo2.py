strt, end = input().split()
strt = int(strt)
end = int(end)
for numb in range(strt,end+1):
	if numb % 2 == 0:
		print(numb, end =' ')
