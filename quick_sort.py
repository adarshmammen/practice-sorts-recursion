def quick_sort(li):
	if len(li)<=1:
		return li
	else:
		return quick_sort([e for e in li[1:] if e<=li[0]]) + [li[0]] + quick_sort([e for e in li[1:] if e>li[0]])

print quick_sort([54,16,35,1,7456,13])