from collections import deque


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": []
}


def bfs(graph, start, goal):
    queue = deque([start])
    visited = set()

    while queue:
        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return True

        for neighbour in graph[node]:
            queue.append(neighbour)

    return False


def dfs(graph, start, goal):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return True

        for neighbour in graph[node]:
            stack.append(neighbour)

    return False


print("BFS Result:", bfs(graph, "A", "G"))
print("DFS Result:", dfs(graph, "A", "G"))