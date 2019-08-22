strt, end = input().split()
strt = int(strt)
end = int(end)
for numb in range(strt+1,end):
	if numb % 2 == 0:
		print(numb, end =' ')
