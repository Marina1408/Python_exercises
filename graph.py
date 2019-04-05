def breadth_first_search(graph, start_vertex):
	visited, versticies = [], [start_vertex]
	if graph and start_vertex and start_vertex in graph:
		while versticies:
			vertex = versticies.pop(0)
			if vertex not in visited:
				visited.append(vertex)
				versticies.extend([v for v in graph[vertex]
						           if v not in visited])
	return visited

graph = {}

def add_graph_vertex(graph, vertex, edges):
	"""  Adds vertex to graph
	"""
	if not edges:
		graph[vertex] = []

	edges = edges.split(',')
	if vertex in graph:
		for edge in edges:
			if edge not in graph[vertex]:
				graph[vertex].append(edge)
	else:
		graph[vertex] = edges

	for edge in edges:
		if edge in graph:
			graph[edge].append(vertex)
		else:
			graph[edge] = [vertex]

graph = {}

while True:
	vertex = input("Please enter graph vertex: ")
	if not vertex:
		continue

	edges = input(f"Please input edges separated by ',' for {vertex}: ")
	add_graph_vertex(graph, vertex, edges)
	print(graph)
	next_vertex = input(("Stop adding versticies? (y/yes). "
		                 "Pres enter for continue: "))
	if next_vertex.lower() in ('y', 'yes'):
		break

while True:
	svertex = input("Please inpup start vertex: ")
	if svertex:
		print(breadth_first_search(graph, svertex))
	else:
		break
