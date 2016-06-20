#This problem was used for: 
#       TopCoder Collegiate Challenge Semifinal Round 4 - Division I, Level One
#TCCC 03 Semifinals Room 4 – Circuits – Div 1 275


'''test = ["1 2 3 4 5","2 3 4 5","3 4 5","4 5","5",""]
cost = ["2 2 2 2 2","2 2 2 2","2 2 2","2 2","2",""]
'''
    	
test = ["1 2","2",""]
cost = ["5 3","7",""]

graph = [[-1 for y in range(len(test))] for x in range(len(test))]
prev_eles = []
for i in range(len(test)):
	splits_1 = test[i].split(" ") 
	splits_cost = cost[i].split(" ") 

	if splits_1 != "" or '':
		for j in range(len(splits_1)):
			if splits_1[j]!= '' or "":
				if prev_eles == []:
					graph[0][int(splits_1[j])] = int(splits_cost[j])
				else:
					graph[int(prev_eles[j])][int(splits_1[j])] = int(splits_cost[j])
		prev_eles = splits_1

main_result = 0
#	else:
#		prev_eles = [ele-1 for ele in splits_1]
for i in range(len(graph)):
	for j in range((len(graph))):

		check = [[False for y in range(len(test))] for x in range(len(test))]

		stack = []
		result = 0

		stack.append(str(i)+" "+str(j))

		while stack!= []:
			top = map(int,(stack.pop()).split(" "))
			print top
			if top[0]<0 or top[0]>len(test)-1:
				continue
			if top[1]<0 or top[1]>len(test)-1:
				continue
			if graph[top[0]][top[1]] == -1:
				continue
			check[top[0]][top[1]] = True
			result+=graph[top[0]][top[1]]

			if (top[0]<len(test)-1 and check[top[0]+1][top[1]]!=True) and (top[1]<len(test)-1 and check[top[1]+1][top[1]]!=True): stack.append(str(top[0]+1)+" "+str(top[1]+1))
			#if top[1]<len(test)-2 and check[top[0]][top[1]+1]!=True: stack.append(str(top[0])+" "+str(top[1]+1))
		if result>main_result:
			main_result = result
print main_result



