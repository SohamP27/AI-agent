from collections import deque
from time import perf_counter_ns


def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    nodes_expanded = 0

    while queue:
        current, path = queue.popleft()
        nodes_expanded += 1

        if current == goal:
            return path, nodes_expanded

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None, nodes_expanded


def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    nodes_expanded = 0

    while stack:
        current, path = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current == goal:
            return path, nodes_expanded

        for neighbor in reversed(graph[current]):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None, nodes_expanded


def profile_search(search_function, graph, start, goal, runs=5000):
    total_time = 0
    final_path = None
    final_nodes = 0

    for _ in range(runs):
        start_time = perf_counter_ns()

        path, nodes = search_function(graph, start, goal)

        end_time = perf_counter_ns()

        total_time += end_time - start_time
        final_path = path
        final_nodes = nodes

    average_time_ns = total_time / runs
    average_time_us = average_time_ns / 1000

    return average_time_us, final_path, final_nodes


def display_result(case_name, graph, start, goal):
    print("\n" + "=" * 55)
    print(case_name)
    print("=" * 55)

    bfs_time, bfs_path, bfs_nodes = profile_search(
        bfs, graph, start, goal
    )

    dfs_time, dfs_path, dfs_nodes = profile_search(
        dfs, graph, start, goal
    )

    print("\nBFS Result")
    print("Path:", " -> ".join(map(str, bfs_path)))
    print("Path Length:", len(bfs_path) - 1)
    print("Nodes Expanded:", bfs_nodes)
    print(f"Average Time: {bfs_time:.3f} microseconds")

    print("\nDFS Result")
    print("Path:", " -> ".join(map(str, dfs_path)))
    print("Path Length:", len(dfs_path) - 1)
    print("Nodes Expanded:", dfs_nodes)
    print(f"Average Time: {dfs_time:.3f} microseconds")


# --------------------------------------------------
# BEST CASE - 5 NODE GRAPH
# --------------------------------------------------

best_graph = {
    0: [1, 2],
    1: [0],
    2: [0, 3],
    3: [2, 4],
    4: [3]
}

display_result(
    "BEST CASE - 5 NODE GRAPH",
    best_graph,
    0,
    1
)


# --------------------------------------------------
# AVERAGE CASE - 10 NODE GRAPH
# --------------------------------------------------

average_graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1, 6],
    4: [1, 7],
    5: [2, 8],
    6: [3, 9],
    7: [4],
    8: [5],
    9: [6]
}

display_result(
    "AVERAGE CASE - 10 NODE GRAPH",
    average_graph,
    0,
    9
)


# --------------------------------------------------
# WORST CASE - 16 NODE GRAPH
# --------------------------------------------------

worst_graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5, 6],
    3: [1, 7],
    4: [1, 8, 9],
    5: [2, 10],
    6: [2, 11, 12],
    7: [3, 13],
    8: [4, 13],
    9: [4, 14],
    10: [5, 14],
    11: [6, 15],
    12: [6],
    13: [7, 8, 15],
    14: [9, 10, 15],
    15: [11, 13, 14]
}

display_result(
    "WORST CASE - 16 NODE GRAPH",
    worst_graph,
    0,
    15
)
