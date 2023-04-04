from egzP9btesty import runtests

def DFS(G,s):
	cykl=[]
	visited=[[0for j in range(len(G))]for i in range(len(G))]
	def DFS_visited(s):
		print(s)
		nonlocal G,cykl,visited
		for i in range(len(G)):
			if G[s][i]==1 and visited[s][i]==0:
				visited[s][i]=1
				#G[s][i]=0
				DFS_visited(i)
		cykl.append(s)
	DFS_visited(s)
	return cykl
def b_graf(G,R):
	graf=[[0for j in range(len(G))]for i in range(len(G))]
	for i in range(len(G)):
		for j in G[i]:
			graf[i][j]=1
	for i in range(len(R)):
		for j in R[i]:
			graf[i][j]=0
	return graf
def dyrektor( G, R ):
	#print(G,R)
	graf=b_graf(G,R)
	print(graf)
	#print(G)
	#print(R)
	cykl = DFS(graf, 0)
	#print(graf)
	#print(cykl)
	#cykl.pop(0)
	return cykl[::-1]
	
runtests(dyrektor, all_tests=False)
