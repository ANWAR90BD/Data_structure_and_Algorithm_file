# BFS implementation here

def bfs(graph, node, queue, visited, level):
    visited.append(node)
    queue.append(node)

    level[node] = 0

    while queue:
        parent = queue.pop(0)

        print(parent, end=" ")


        for child in graph[parent]:
            if child not in visited:
                visited.append(child)
                queue.append(child)
                level[child] = level[parent] + 1




if __name__ == "__main__":
    queue = []
    visited = []
    level = {}

    graph = {
        'S' : ['T', 'U'],
        'T' : ['V', 'W'],
        'U' : ['X'],
        'V' : [],
        'W' : ['X'],
        'X' : []
    }

    bfs(graph, 'S', queue, visited, level)
    print("\n", level)