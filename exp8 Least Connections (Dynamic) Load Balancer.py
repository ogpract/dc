class LeastConnectionsLoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.connections = {server: 0 for server in servers}

    def get_least_loaded_server(self):
        min_server = min(self.connections.items(), key=lambda x: x[1])[0]
        return min_server

    def assign_task(self):
        server = self.get_least_loaded_server()
        self.connections[server] += 1
        return server

    def complete_task(self, server):
        if server in self.servers and self.connections[server] > 0:
            self.connections[server] -= 1


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

    lb = LeastConnectionsLoadBalancer(servers)

    print("\nTask Distribution:")
    for i in range(num_tasks):
        server = lb.assign_task()
        print(f"Task {i+1} assigned to {server} (Current connections: {lb.connections[server]})")

    print("\nFinal Connection Distribution:")
    for server, count in lb.connections.items():
        print(f"{server}: {count} active connections")


if __name__ == "__main__":
    main()

# output format:
# Enter number of servers: 3
# Enter number of tasks to distribute: 7