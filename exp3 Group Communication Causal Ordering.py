import threading
import time
import queue

class NodeCausalOrder:
    def __init__(self, node_id, nodes):
        self.node_id = node_id
        self.nodes = nodes  # List of other nodes
        self.state = 0  # State that will be updated
        self.msg_queue = queue.Queue()  # Queue for incoming messages
        self.vector_clock = [0] * len(nodes)  # Vector clock for causal ordering

    def broadcast(self, msg):
        for node in self.nodes:
            node.receive_message(msg)

    def receive_message(self, msg):
        print(f"Node {self.node_id} received message: {msg}")
        
        for i in range(len(self.vector_clock)):
            self.vector_clock[i] = max(self.vector_clock[i], msg['vector_clock'][i])
        
        self.vector_clock[self.node_id] += 1
        self.state = msg['state']
        
        print(f"Node {self.node_id} updated state to {self.state} with vector clock: {self.vector_clock}")

    def update_state(self):
        self.vector_clock[self.node_id] += 1  # Increment own vector clock before broadcasting
        self.state += 1  # Update state
        msg = {'node_id': self.node_id, 'state': self.state, 'vector_clock': self.vector_clock}
        
        if self.node_id == 0:
            print(f"Node {self.node_id} broadcasting state: {self.state} with vector clock: {self.vector_clock}")
            self.broadcast(msg)

def node_thread_causal_order(node, stop_event):
    while not stop_event.is_set():
        time.sleep(2)
        node.update_state()

if __name__ == '__main__':
    nodes = [NodeCausalOrder(i, []) for i in range(3)]
    
    for i, node in enumerate(nodes):
        node.nodes = [n for j, n in enumerate(nodes) if j != i]
    
    for node in nodes:
        node.vector_clock = [0] * len(nodes)  # Correctly re-initialize vector clocks

    stop_event = threading.Event()

    threads = []
    for node in nodes:
        thread = threading.Thread(target=node_thread_causal_order, args=(node, stop_event))
        threads.append(thread)
        thread.start()

    time.sleep(7)
    stop_event.set()  # Signal the threads to stop

    for thread in threads:
        thread.join()

    print("Program finished.")
