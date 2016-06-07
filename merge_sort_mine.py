def mergesort(li):

	if len(li) > 1:
		mid = len(li)/2
		left_half, right_half = li[:mid], li[mid:]

		mergesort(left_half)
		mergesort(right_half)

		i,j,k = 0,0,0

		while i < len(left_half) and j < len(right_half):
			if left_half[i] < right_half[j]:
				li[k] = left_half[i]
				i+=1
			else:
				li[k] = right_half[j]
				j+=1
			k+=1

		while i < len(left_half):
			li[k] = left_half[i]
			i+=1
			k+=1

		while j < len(right_half):
			li[k] = right_half[j]
			j+=1
			k+=1

	return li

print mergesort([2,6,135,75,1345,754,2,0]*100000)