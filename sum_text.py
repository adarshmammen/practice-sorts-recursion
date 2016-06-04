def sum_text():
	a = open('integers.txt','r')
	z =  a.read()
	li = z.split()
	add = map(int,li)
	final = sum(add)
	return final

def odds():
		li = [e for e in range(1,100) if e%2 != 0]
		return li

def quick_sort(li):
	if len(li) <=1:
		return li
	else:
		return quick_sort([e for e in li[1:] if e<=li[0]]) + [li[0]] + quick_sort([e for e in li[1:] if e> li[0]])

def find_max(li):
	maxer= 0
	for i in li:
		if i> maxer:
			maxer = i
	return maxer

def bit_count( v ):
    c = 0
    while v > 0:
        v &= v - 1
        c += 1
    return c

print sum_text()
print odds()
a = quick_sort([52,1,6,586,23412346,6,2])
print a[-1]
print find_max([52,1,6,586,23412346,6,2])
print bit_count(15)
