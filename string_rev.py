def quicksort(s):
	if len(s) <= 1:
		return s
	else:
		return quicksort([ele for ele in s[1:] if ele>=s[0]]) + [s[0]] + quicksort([ele for ele in s[1:] if ele<s[0]])

def merge(l):
	if len(l)<=1:
		return l
	else:
		mid = len(l)/2
		left = l[:mid]
		right = l[mid:]

		merge(left)
		merge(right)

		i,j,k = 0,0,0

		while i < len(left) and j < len(right):
			if left[i]<=right[j]:
				l[k] = left[i]
				k+=1
				i+=1
			else:
				l[k] = right[j]
				j+=1
				k+=1
		while i < len(left):
			l[k] = left[i]
			k+=1
			i+=1
		while j < len(right):
			l[k] = right[j]
			k+=1
			j+=1

		return l

def rev(s):
	if len(s)<=1:
		return s
	else:
		return rev(s[-1]) + rev(s[:-1]) 

def spaces(s):
	if not s:
		return 0
	else:
		return 1 + spaces(s[1:]) if s[0]== " " else 0 + spaces(s[1:])

def combinations(n, list, combos=[]):
    # initialize combos during the first pass through
    if combos is None:
        combos = []

    if len(list) == n:
        # when list has been dwindeled down to size n
        # check to see if the combo has already been found
        # if not, add it to our list
        if combos.count(list) == 0:
            combos.append(list)
            combos.sort()
        return combos
    else:
        # for each item in our list, make a recursive
        # call to find all possible combos of it and
        # the remaining items
        for i in range(len(list)):
            refined_list = list[:i] + list[i+1:]
            combos = combinations(n, refined_list, combos)
        return combos


#print merge([1,5,2,6])

print combinations(2,[4,3,1])

print spaces("sgb")