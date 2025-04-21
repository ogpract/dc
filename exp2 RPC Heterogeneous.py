# client code:
import xmlrpc.client

def connect_to_server():
    try:
        server = xmlrpc.client.ServerProxy('http://127.0.0.1:8000')
        permission = server.ask_permission('Client_PC')

        if not permission:
            print("Connection denied by the server. Please try again later.")
            return None

        return server
    except (xmlrpc.client.Fault, ConnectionRefusedError) as e:
        print("Error connecting to the server: ", e)
        return None

def add(a, b, server):
    return server.add_numbers(a, b)

def multiply(a, b, server):
    return server.multiply(a, b)

def subtract(a, b, server):
    return server.subtract(a, b)

def divide(a, b, server):
    return server.divide(a, b)

def request_connection():
    while True:
        server = connect_to_server()

        if server:
            return server
        else:
            response = input("Do you want to retry connecting to the server? (yes/no): ")
            if response.lower() == 'no':
                print("Exiting the client.")
                break
            elif response.lower() != 'yes':
                print("Invalid option. Please enter 'yes' or 'no'.")

def main():
    server = request_connection()

    if server:
        print("Calculator Client")

        while True:
            print("\nOptions:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exit")

            choice = input("Select operation (1-5): ")
            if choice in ['1', '2', '3', '4']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print("Result: ", add(num1, num2, server))
                elif choice == '2':
                    print("Result: ", subtract(num1, num2, server))
                elif choice == '3':
                    print("Result: ", multiply(num1, num2, server))
                elif choice == '4':
                    print("Result: ", divide(num1, num2, server))
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid input. Please select a valid option.")
    else:
        print("Unable to connect to the server.")

if __name__ == "__main__":
    main()


# server code:
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer(('0.0.0.0', 8000), requestHandler=RequestHandler)
server.register_introspection_functions()

def ask_permission(client_address):
    response = input(f"{client_address} is requesting to connect. Do you accept? (yes/no): ")
    return response.lower() == 'yes'

def add_numbers(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    else:
        return a / b

server.register_function(add_numbers, 'add_numbers')
server.register_function(multiply, 'multiply')
server.register_function(subtract, 'subtract')
server.register_function(divide, 'divide')
server.register_function(ask_permission, 'ask_permission')

print("Server is running on port 8000...")
server.serve_forever()