graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}
 
visited = []

def dfs(graph, vertex):
	if vertex not in visited:
		visited.append(vertex)
		for v in graph[vertex]:
			dfs(graph, v)


svertex = input("Please inpup start vertex: ")
dfs(graph, svertex)
print(visited)

