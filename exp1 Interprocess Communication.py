# client code:
import socket

def send_numbers(num1, num2):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))  # Connect to the server on localhost
    client_socket.send(f"{num1} {num2}".encode())
    result = client_socket.recv(1024).decode()
    print(f"The sum of {num1} and {num2} is: {result}")
    client_socket.close()

if __name__ == "__main__":
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    send_numbers(a, b)


# server code:
import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)
    print("Server is listening on port 12345...")
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        data = client_socket.recv(1024).decode()
        num1, num2 = map(int, data.split())
        result = num1 + num2
        client_socket.send(str(result).encode())
        client_socket.close()

if __name__ == "__main__":
    start_server()
