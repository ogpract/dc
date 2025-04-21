import threading
import time
import queue

class NodeConsistentOrder:
    def __init__(self, node_id, nodes):
        self.node_id = node_id
        self.nodes = nodes  # List of other nodes
        self.state = 0  # State that will be updated
        self.msg_queue = queue.Queue()  # Queue for incoming messages
        self.message_counter = 0  # Global counter for consistent ordering
        self.received_messages = 0  # Track the number of messages received

    def broadcast(self, msg):
        for node in self.nodes:
            node.receive_message(msg)

    def receive_message(self, msg):
        print(f"Node {self.node_id} received message: {msg}")
        
        self.msg_queue.put(msg)
        self.received_messages += 1

    def process_messages(self):
        while not self.msg_queue.empty():
            msg = self.msg_queue.get()
            self.state = msg['state']
            self.message_counter = msg['message_counter']
            print(f"Node {self.node_id} updated state to {self.state} with message_counter: {self.message_counter}")

    def update_state(self):
        self.message_counter += 1
        self.state += 1  # Update state
        msg = {'node_id': self.node_id, 'state': self.state, 'message_counter': self.message_counter}
        
        if self.node_id == 0:
            print(f"Node {self.node_id} broadcasting state: {self.state} with message_counter: {self.message_counter}")
            self.broadcast(msg)

def node_thread_consistent_order(node, stop_event):
    while not stop_event.is_set():
        time.sleep(3)
        node.update_state()
        node.process_messages()

if __name__ == '__main__':
    nodes = [NodeConsistentOrder(i, []) for i in range(3)]
    
    for i, node in enumerate(nodes):
        node.nodes = [n for j, n in enumerate(nodes) if j != i]

    stop_event = threading.Event()

    threads = []
    for node in nodes:
        thread = threading.Thread(target=node_thread_consistent_order, args=(node, stop_event))
        threads.append(thread)
        thread.start()

    time.sleep(10)
    stop_event.set()  # Signal the threads to stop

    for thread in threads:
        thread.join()

    print("Program finished.")
