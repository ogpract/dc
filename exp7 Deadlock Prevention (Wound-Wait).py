def prevent_deadlock(n, m):
    print("\n--- Deadlock Prevention (Wound-Wait) ---")
    timestamps = list(map(int, input(f"Enter timestamps for {n} processes (space-separated): ").split()))
    if len(timestamps) != n:
        print(f"Error: Please enter exactly {n} timestamps.")
        return

    resources = [None] * m
    num_requests = m
    for _ in range(num_requests):
        p, r = map(int, input("Enter request (process resource): ").split())
        if resources[r] is None:
            resources[r] = p
            print(f"P{p} requests R{r}: granted")
        else:
            holder = resources[r]
            if timestamps[p] < timestamps[holder]:
                print(f"P{p} requests R{r} (held by P{holder}): P{p} wounds P{holder}, P{holder} aborts")
                resources[r] = p
            else:
                print(f"P{p} requests R{r} (held by P{holder}): P{p} waits")
if __name__ == "__main__":
    n = int(input("Enter number of processes: "))
    m = int(input("Enter number of resources: "))
    prevent_deadlock(n, m)
    

# output format:
# Enter number of processes: 3
# Enter number of resources: 3

# --- Deadlock Prevention (Wound-Wait) ---
# Enter timestamps for 3 processes (space-separated): 2 6 4
# Enter request (process resource): 1 0
# P1 requests R0: granted
# Enter request (process resource): 2 0
# P2 requests R0 (held by P1): P2 wounds P1, P1 aborts
# Enter request (process resource): 0 1
# P0 requests R1: granted