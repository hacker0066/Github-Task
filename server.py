import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define host and port
    host = 'localhost'
    port = 12345
    
    # Bind the socket
    server_socket.bind((host, port))
    
    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")
    
    while True:
        # Accept connection
        client_socket, address = server_socket.accept()
        print(f"Connection from {address}")
        
        try:
            while True:
                # Receive data from client
                data = client_socket.recv(1024).decode()
                if not data:
                    break
                
                print(f"Received from client: {data}")
                
                # Send response back to client
                response = f"Server received: {data}"
                client_socket.send(response.encode())
                
        except ConnectionResetError:
            print("Client disconnected")
        finally:
            client_socket.close()

if __name__ == "__main__":
    start_server()