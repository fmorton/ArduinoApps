import socket

def run_server():
    # 1. Define host and port (127.0.0.1 is local loopback)
    HOST = '0.0.0.0'
    PORT = 65432        # Non-privileged ports are > 1023

    # 2. Create a socket object
    # AF_INET = IPv4, SOCK_STREAM = TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        
        # Allow instant reuse of the port after restarting the server
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # 3. Bind the socket to the address and port
        server_socket.bind((HOST, PORT))
        
        # 4. Listen for incoming connections
        server_socket.listen()
        print(f"Server is listening on {HOST}:{PORT}...")

        # 5. Accept a connection (blocks until a client connects)
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected established with client at: {addr}")
            
            # 6. Receive and echo data loop
            while True:
                data = conn.recv(1024) # Receive up to 1024 bytes
                if not data:
                    break # Client closed the connection
                
                print(f"Received from client: {data.decode('utf-8')}")
                
                # Send the data back to the client
                conn.sendall(data)
                
    print("Server shut down cleanly.")

if __name__ == "__main__":
    run_server()
