
import socket

def start_client():
    host = 'localhost'  # Server hostname or IP address
    port = 12345        # Server port

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))
    print(f"Connected to {host}:{port}")

    # Send message to the server
    message = "Hello, server!"
    client_socket.send(message.encode())

    # Receive response from the server
    response = client_socket.recv(1024).decode()
    print(f"Received response from server: {response}")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client()