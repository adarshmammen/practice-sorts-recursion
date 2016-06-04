def fib(n):
	if n==1 or n==0:
		return 1 if n==1 else 0
	else:
		return fib(n-1)+fib(n-2)

a = [fib(e) for e in range(20)]
print a