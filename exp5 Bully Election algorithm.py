import random
import time
import threading

class Process(threading.Thread):
    def __init__(self, pid, manager):
        super().__init__()
        self.pid = pid
        self.manager = manager
        self.active = True
        self.coordinator_id = None

    def run(self):
        time.sleep(random.uniform(0.1, 0.5))

    def set_inactive(self):
        self.active = False
        print(f"P{self.pid} has become Inactive")

    def is_active(self):
        return self.active

    def is_coordinator_alive(self):
        return self.manager.is_alive(self.coordinator_id)

    def set_coordinator(self, cid):
        self.coordinator_id = cid

    def initiate_election(self):
        print(f"P{self.pid} initiates Election")
        higher = [p for p in self.manager.processes[self.pid+1:] if p.is_active()]
        for p in higher:
            print(f"P{self.pid} -> Election -> P{p.pid}")
            p.receive_election()
        if not higher:
            self.become_coordinator()

    def receive_election(self):
        if self.active:
            print(f"P{self.pid} -> Alive")
            time.sleep(0.5)
            self.initiate_election()

    def become_coordinator(self):
        print(f"P{self.pid} becomes Coordinator")
        for p in self.manager.processes:
            if p.pid != self.pid:
                print(f"P{self.pid} -> Coordinator -> P{p.pid}")
                p.set_coordinator(self.pid)

class Manager:
    def __init__(self, n):
        self.processes = [Process(i, self) for i in range(n)]
        for p in self.processes:
            p.set_coordinator(n - 1)

    def is_alive(self, pid):
        return self.processes[pid].is_active()

    def start(self):
        for p in self.processes:
            p.start()

def main():
    n = 5
    mgr = Manager(n)
    mgr.start()

    print(f"P{n - 1} is initially Coordinator")
    mgr.processes[n - 1].set_inactive()

    active = [p for p in mgr.processes[:-1] if p.is_active()]
    initiator = random.choice(active)

    if not initiator.is_coordinator_alive():
        print(f"P{initiator.pid} detects Coordinator failure")
        initiator.initiate_election()

if __name__ == "__main__":
    main()
