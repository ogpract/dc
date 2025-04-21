# client code:
import xmlrpc.client

server = xmlrpc.client.ServerProxy('http://127.0.0.1:8000')

def add(a, b):
    return server.add_numbers(a, b)

def multiply(a, b):
    return server.multiply(a, b)

def subtract(a, b):
    return server.subtract(a, b)

def divide(a, b):
    return server.divide(a, b)

if __name__ == "__main__":
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
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid input. Please select a valid option.")


# server code:
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer(('0.0.0.0', 8000), requestHandler=RequestHandler)
server.register_introspection_functions()

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

print("Server is running on port 8000...")
server.serve_forever()