def add_vertex(v):
    global graph
    if v in graph:
        print("this vertex already exists")
    else:
        graph[v] = []


def add_edge(v1, v2, w):
    global graph
    if v1 not in graph:
        print("vertex ", v1, " dose not exist")
    elif v2 not in graph:
        print("vertex ", v2, " dose not exist")
    else:
        temp=[v2, w]
        graph[v1].append(temp)


def print_graph():
    global graph
    for v in graph:
        for i in graph[v]:
            print(v, "->", i[0], "with weight", i[1])


graph = {}
print("insert the vertices of the graph")
add_vertex(1)
add_vertex(2)
add_vertex(3)
add_vertex(4)
print("insert the edges")
add_edge(1, 2, 1)
add_edge(1, 3, 2)
add_edge(2, 3, 1)
add_edge(3, 4, 5)
add_edge(4, 1, 4)
print_graph()
print(graph)
