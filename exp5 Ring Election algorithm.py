class RingElection:
    def __init__(self, processes):
        self.processes = processes  # List of process IDs
        self.n = len(processes)
        self.coordinator = max(processes)  # Initially assume highest ID is coordinator

    def start_election(self, initiator_index):
        print(f"\nElection started by Process {self.processes[initiator_index]}")
        election_list = []
        current_index = initiator_index

        while True:
            next_index = (current_index + 1) % self.n
            current_process = self.processes[current_index]
            next_process = self.processes[next_index]

            print(f"Process {current_process} sends election message to Process {next_process}")
            if next_process not in election_list:
                election_list.append(next_process)
            if next_index == initiator_index:
                break
            current_index = next_index

        new_coordinator = max(election_list)
        self.coordinator = new_coordinator
        print(f"Election complete. New Coordinator is Process {self.coordinator}")

    def get_coordinator(self):
        return self.coordinator


# Sample Usage
if __name__ == "__main__":
    processes = [1, 3, 4, 7, 10]  # Unique IDs of processes
    ring = RingElection(processes)

    print(f"Initial Coordinator: Process {ring.get_coordinator()}")

    initiator = 2  # Index of process 4
    ring.start_election(initiator)

    print(f"Updated Coordinator: Process {ring.get_coordinator()}")
