import time

def print_queue(queue):
    items = [f"Timestamp {ts} P{p}" for ts, p in queue]
    print(f"Queue: [{', '.join(items)}]")

n = int(input("Enter the number of processes: "))
p = int(input("Enter the first process to enter CS: "))
q = int(input("Enter the second process to enter CS: "))

others_p = [i for i in range(1, n + 1) if i != p]  # All processes except p
others_q = [i for i in range(1, n + 1) if i != q]  # All processes except q
repliers_to_q = [i for i in others_q if i != p]    # All processes except p and q

queue = [(0, p), (1, q)]  # Timestamp 0 for p, 1 for q

print("\nInitial Queue State:")
print_queue(queue)

print(f"P{p} sends request message to {', '.join([f'P{i}' for i in others_p])}")
print(f"P{q} sends request message to {', '.join([f'P{i}' for i in others_q])}")
print(f"P{p} receives reply from {', '.join([f'P{i}' for i in others_p])}")
if repliers_to_q:
    print(f"P{q} receives reply from {', '.join([f'P{i}' for i in repliers_to_q])}")

while queue:
    print("\nQueue before entering Critical Section:")
    print_queue(queue)
    ts, current_process = queue[0]
    if current_process == p:
        print(f"P{p} enters Critical Section")
        time.sleep(4)
        print(f"P{p} exits Critical Section")
        print(f"P{p} sends reply to P{q}")
    else:
        print(f"P{q} enters Critical Section")
        time.sleep(5)
        print(f"P{q} exits Critical Section")

    queue = queue[1:]  

print("Done")

# output format:
# Enter the number of processes: 3
# Enter the first process to enter CS: 1
# Enter the second process to enter CS: 3