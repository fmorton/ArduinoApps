import socket

# Configure server coordinates
HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 65432      # Arbitrary non-privileged port (>1023)

# Create a TCP/IP socket (AF_INET = IPv4, SOCK_STREAM = TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    
    # Allow immediate reuse of the port after termination (avoids "Address already in use" errors)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Associate the socket with the host address and port
    server_socket.bind((HOST, PORT))
    
    # Enable the server to accept connections (backlog queue size = 5)
    server_socket.listen(5)
    print(f"[*] Server listening on {HOST}:{PORT}...")
    
    # Keep the server running continuously
    while True:
        try:
            # Block and wait for an incoming connection request
            client_socket, client_address = server_socket.accept()
            print(f"[+] Accepted connection from {client_address[0]}:{client_address[1]}")
            
            # Manage the active client connection safely
            with client_socket:
                while True:
                    # Receive data packets up to 1024 bytes
                    data = client_socket.recv(1024)
                    
                    # If client disconnects, recv() returns an empty byte string
                    if not data:
                        print(f"[-] Connection closed by {client_address[0]}")
                        break
                    
                    # Process and handle binary data transmission explicitly
                    message = data.decode('utf-8')
                    print(f"[Received] {message}")
                    
                    # Echo back a response acknowledgment (must be encoded back to bytes)
                    response = f"Server ACK: {message}"
                    client_socket.sendall(response.encode('utf-8'))
                    
        except KeyboardInterrupt:
            print("\n[*] Shutting down the listener script.")
            break
