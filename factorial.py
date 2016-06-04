def factorial(n):
	if n ==1:
		return 1
	else:
		ret =  n * factorial(n-1)
		print ret
		return ret
factorial(10)