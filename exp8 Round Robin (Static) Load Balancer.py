class RoundRobinLoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.current_server = 0

    def get_next_server(self):
        server = self.servers[self.current_server]
        self.current_server = (self.current_server + 1) % len(self.servers)
        return server


def main():
    try:
        num_servers = int(input("Enter number of servers: "))
        if num_servers <= 0:
            raise ValueError("Number of servers must be positive!")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    servers = [f"S{i+1}" for i in range(num_servers)]

    try:
        num_tasks = int(input("Enter number of tasks to distribute: "))
        if num_tasks <= 0:
            raise ValueError("Number of tasks must be positive!")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    lb = RoundRobinLoadBalancer(servers)
    assignments = {server: 0 for server in servers}

    print("\nTask Distribution:")
    for i in range(num_tasks):
        server = lb.get_next_server()
        assignments[server] += 1
        print(f"Task {i+1} assigned to {server}")

    print("\nLoad Distribution Summary:")
    for server, count in assignments.items():
        print(f"{server}: {count} tasks")


if __name__ == "__main__":
    main()

# output format:
# Enter number of servers: 3
# Enter number of tasks to distribute: 7