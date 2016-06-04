def fib(n):
	if n == 0 or n==1:
		return 1 if n==1 else 0
	else:
		return fib(n-1) + fib(n-2)

def expo(x,n):
	if n ==0 or n==1:
		return 1 if n==0 else x
	else:
		return x*expo(x,n-1)


def flatten(li, result=[]):
	for i in li:
		if isinstance(i,list):
			flatten(i,result)
		else:
			result.append(i)
	return result

def flatten_dict(dicti, lkey = '', result={}):
	for i,v in dicti.items():
		key = lkey + i 
		if isinstance(v,dict):
			flatten_dict(v, key+'.')
		else:
			result[key]=v
	return result

def quick_sort(li,result=[]):
	if len(li)<=1:
		return li
	else:
		return quick_sort([e for e in li[1:] if e<=li[0]]) + [li[0]] + quick_sort([e for e in li[1:] if e>li[0]])

print quick_sort([12,3,6])


#print flatten([1,2,[3,4],5,[[3,4],5],6,4])
#print flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})

