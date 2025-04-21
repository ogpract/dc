def avoid_deadlock(n, m):
    print("\n--- Deadlock Avoidance ---")
    max_demand = []
    allocation = []

    print(f"Enter maximum demand for each process ({m} resources):")
    for i in range(n):
        max_demand.append(list(map(int, input(f"Process {i}: ").split())))

    print(f"Enter current allocation for each process ({m} resources):")
    for i in range(n):
        allocation.append(list(map(int, input(f"Process {i}: ").split())))

    available = list(map(int, input(f"Enter available resources ({m} values): ").split()))
    need = [[max_demand[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]

    finish = [False] * n
    safe_seq = []
    work = available[:]

    while len(safe_seq) < n:
        found = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                for j in range(m):
                    work[j] += allocation[i][j]
                finish[i] = True
                safe_seq.append(i)
                found = True
                break
        if not found:
            break

    if len(safe_seq) == n:
        print("System is in a safe state.")
        print("Safe sequence:", safe_seq)
    else:
        print("System is not in a safe state.")
if __name__ == "__main__":
    n = int(input("Enter number of processes: "))
    m = int(input("Enter number of resources: "))
    avoid_deadlock(n, m)
    
# output format:
# Enter number of processes: 3
# Enter number of resources: 3

# --- Deadlock Avoidance ---
# Enter maximum demand for each process (3 resources):
# Process 0: 2 2 4
# Process 1: 2 1 3
# Process 2: 3 4 1
# Enter current allocation for each process (3 resources):
# Process 0: 1 2 1
# Process 1: 2 0 1
# Process 2: 2 2 1
# Enter available resources (3 values): 0 1 2
# System is in a safe state.
# Safe sequence: [1, 0, 2]