
import socket

def start_server():
    host = 'localhost'  # Localhost or 0.0.0.0 for all interfaces
    port = 12345        # Arbitrary non-privileged port

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        # Wait for a connection
        client_socket, address = server_socket.accept()
        print(f"Connection from {address} has been established.")

        # Receive data from the client
        data = client_socket.recv(1024).decode()
        print(f"Received message from client: {data}")

        # Send response back to the client
        response = "Hello, client!"
        client_socket.send(response.encode())

        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    start_server()