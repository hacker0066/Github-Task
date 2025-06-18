import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define host and port
    host = 'localhost'
    port = 12345
    
    try:
        # Connect to the server
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")
        
        while True:
            # Get user input
            message = input("Enter message (or 'quit' to exit): ")
            
            if message.lower() == 'quit':
                break
            
            # Send data to server
            client_socket.send(message.encode())
            
            # Receive response from server
            response = client_socket.recv(1024).decode()
            print(f"Server response: {response}")
            
    except ConnectionRefusedError:
        print("Could not connect to server. Make sure the server is running.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()