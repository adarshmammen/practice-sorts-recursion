def mul3(n):
	if n == 1:
		return 3
	else:
		return 3 +  mul3(n-1)
		
print mul3(10)