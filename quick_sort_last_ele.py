def quicksort(n):
	if len(n) <=1:
		return n
	else:
		return quicksort([e for e in n[-2::-1] if e<=n[-1]]) + [n[-1]] + quicksort([e for e in n[-2::-1] if e>n[-1] ])

print quicksort([5,3,135,7,23435,5])