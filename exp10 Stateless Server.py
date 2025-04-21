# client.py
import socket

def stateless_client(start_pos):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 8888))
    client.sendall(str(start_pos).encode())
    data = client.recv(1024).decode()
    print(f"Received: {data}")
    client.close()

if __name__ == "__main__":
    stateless_client(0)      # First call
    stateless_client(50)     # Second call


# server.py
import socket
import threading

def handle_client(conn, filename):
    try:
        request = conn.recv(1024).decode().strip()
        start_pos = int(request)

        with open(filename, "r") as file:
            file.seek(start_pos)
            data = file.read()

        response = f"{data}"
    except Exception as e:
        response = f"Error: {str(e)}"

    conn.sendall(response.encode())
    conn.close()

def stateless_server():
    filename = "data.txt"
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 8888))
    server.listen(5)
    print("Stateless Server is running on port 8888...")

    while True:
        conn, _ = server.accept()
        threading.Thread(target=handle_client, args=(conn, filename)).start()

if __name__ == "__main__":
    stateless_server()


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