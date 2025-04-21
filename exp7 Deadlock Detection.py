def has_cycle(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)

    visited = [False] * n
    rec_stack = [False] * n
    cycle_nodes = []

    def dfs(node, path):
        visited[node] = True
        rec_stack[node] = True
        path.append(node)

        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, path):
                    return True
            elif rec_stack[neighbor]:
                cycle_nodes.extend(path[path.index(neighbor):])
                return True

        rec_stack[node] = False
        path.pop()
        return False

    for i in range(n):
        if not visited[i]:
            if dfs(i, []):
                break

    return cycle_nodes if cycle_nodes else None


def detect_deadlock(n):
    print("\n--- Deadlock Detection and Recovery ---")
    edges = []
    num_edges = int(input("Enter number of wait-for edges: "))
    for _ in range(num_edges):
        u, v = map(int, input("Enter edge (u v) where Pu waits for Pv: ").split())
        edges.append((u, v))

    cycle_nodes = has_cycle(n, edges)
    if cycle_nodes:
        print("Deadlock detected! Processes involved:", cycle_nodes)
        victim = cycle_nodes[0]
        print(f"Recovering from deadlock by aborting process P{victim}.")
        edges = [(u, v) for u, v in edges if u != victim]
        cycle_nodes = has_cycle(n, edges)
        if cycle_nodes:
            print("Deadlock still present, further action needed.")
        else:
            print("Deadlock resolved. Remaining wait-for edges:", edges)
    else:
        print("No deadlock detected.")

if __name__ == "__main__":
    n = int(input("Enter number of processes: "))
    detect_deadlock(n)
    
    
# output format:
# Enter number of processes: 3

# --- Deadlock Detection and Recovery ---
# Enter number of wait-for edges: 3
# Enter edge (u v) where Pu waits for Pv: 0 1
# Enter edge (u v) where Pu waits for Pv: 1 2
# Enter edge (u v) where Pu waits for Pv: 2 0