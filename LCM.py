def LCM(a,b):
	from GCD import gcd
	return a*b/gcd(a,b)

print LCM(20,2)
