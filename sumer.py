def summer(n):
	if n == 1:
		return 1
	else:
		ret =  n+summer(n-1)
		print ret
		return ret
print summer(10)