graph = [[1,0,1],[1,1,0],[1,0,0],[1,1,1]]
visited = [[False for x in range(3)] for y in range(4)]
def dfs():
	stack = []
	path = []
	x,y = 0,0
	visited[x][y]=True
	stack.append(str(x)+str(",")+str(y))
	while stack!= []:
		print stack

		if x==3 and y ==2: #stop condition
			print "Found!"
			stack.pop(0)
			stack.append(str(x)+str(",")+str(y))
			while stack!=[]:
				path.append(stack.pop(0))
			return path
		elif x>0 and visited[x-1][y]==False and graph[x-1][y]==1: #movement
			stack.append(str(x)+str(",")+str(y))
			x-=1
			visited[x][y]=True
		elif y<2 and visited[x][y+1]==False and graph[x][y+1]==1:
			stack.append(str(x)+str(",")+str(y))
			y+=1
			visited[x][y]=True
		elif y>0 and visited[x][y-1]==False and graph[x][y-1]==1:
			stack.append(str(x)+str(",")+str(y))
			y-=1
			visited[x][y]=True
		elif x<3 and visited[x+1][y]==False and graph[x+1][y]==1:
			stack.append(str(x)+str(",")+str(y))
			x+=1
			visited[x][y]=True
		else: # backtrack
			visited[x][y]=True
			ele = stack.pop()
			ind = map(int,ele.split(","))
			x,y=ind[0],ind[1]
			#stack.append(str(x)+str(",")+str(y))

	print "Undiscovered"
	return path	

print dfs()
