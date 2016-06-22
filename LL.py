class LL:
	def __init__(self,val1=0):
		self.val = val1
		self.next = None
		self.prev = None

	def get(self):
		return self.val

	def set(self,val1):
		self.val = val1


l = LL(2)
l.next = LL(3)
l.next.next = LL(4)
l.next.next.next = l


temp = l.next
l.next= LL(10)
l.next.next = temp

for i in range(10):
	print l.val
	l = l.next



def quicksort(li):
	if len(li)<=1:
		return li
	else:
		return quicksort([ele for ele in li[1:] if ele<li[0]]) + [li[0]] + quicksort([ele for ele in li[1:] if ele>=li[0]])


def mergesort(li):
	if len(li)>1:
		mid = len(li)/2
		left = li[:mid]
		right = li[mid:]

		mergesort(left)
		mergesort(right)

		i,j,k = 0,0,0

		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				li[k] = left[i]
				i+=1
			else:
				li[k] = right[j]
				j+=1
			k+=1

		while i < len(left):
			li[k] = left[i]
			i+=1
			k+=1
		while j < len(right):
			li[k] = right[j]
			j+=1
			k+=1

	return li

def fib(n):
	if n == 0:
		return 0
	if n==1:
		return 1
	else:
		return fib(n-1)+fib(n-2)

for i in range(10,0,-1):
	print fib(i)


print quicksort([1,4234,5,135,7,234])
print mergesort([1,4234,5,135,7,234])