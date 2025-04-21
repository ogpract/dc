# client.py
import socket

def stateful_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 9999))
    data = client.recv(1024).decode()
    print(f"Received: {data}")
    client.close()

if __name__ == "__main__":
    stateful_client()

# server.py
import socket
import threading
import json
import os

POSITIONS_FILE = "positions.txt"

def load_positions():
    if os.path.exists(POSITIONS_FILE):
        with open(POSITIONS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_positions(positions):
    with open(POSITIONS_FILE, "w") as file:
        json.dump(positions, file)

client_positions = load_positions()

def handle_client(conn, addr, filename):
    global client_positions
    if addr[0] not in client_positions:
        client_positions[addr[0]] = 0

    try:
        with open(filename, "r") as file:
            file.seek(client_positions[addr[0]])
            data = file.read(40)  # read next chunk
            client_positions[addr[0]] = file.tell()
            save_positions(client_positions)
    except Exception as e:
        data = f"Error: {str(e)}"

    conn.sendall(data.encode())
    conn.close()

def stateful_server():
    filename = "data.txt"
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 9999))
    server.listen(5)
    print("Stateful Server is running on port 9999...")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr, filename)).start()

if __name__ == "__main__":
    stateful_server()

# data.txt
'''The quick brown fox jumps over the lazy dog. 
Python is a powerful and easy-to-learn programming language. 
Stateless and stateful systems have different use cases in computing.'''


# ----------------------------------------------------------------------------------------------
# 1) Create the following files:
# client.py
# server.py
# data.txt

# 2) In data.txt, add given content.

# 3) Run the server:

# 4) Run the client (in a separate terminal):

# 📝 The client will read 20 characters at a time and remember the read position via positions.txt