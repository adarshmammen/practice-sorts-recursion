def todec(n):
	result = 0
	multi=1
	while n!=0:
		result+=n%10*multi
		multi*=2
		n//=10
	return result

def tobin(n):
	result =0
	multi = 1
	while n!=0:
		result+= n % 2 *multi
		multi*=10
		n//=2
	return result

print todec(1111)
print tobin(16)