import socket
import time

from arduino.app_utils import App

print("Hello world!")

def run_client():
    HOST = '192.168.7.90'  # The server's hostname or IP address
    PORT = 65432        # The port used by the server

    # 1. Create a socket object (ConnectionRefusedError)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        
        print(f"Connecting to server at {HOST}:{PORT}...")
        # 2. Connect to the server
        client_socket.connect((HOST, PORT))
        
        # 3. Send data
        message = "Hello, Server! This is the Client."
        client_socket.sendall(message.encode('utf-8'))
        print(f"Sent to server: {message}")
        
        # 4. Receive data back from the server
        data = client_socket.recv(1024)
        
    print(f"Received back from server: {data.decode('utf-8')}")


def loop():
    """This function is called repeatedly by the App framework."""
    # You can replace this with any code you want your App to run repeatedly.
    pass
    #run_client()


# See: https://docs.arduino.cc/software/app-lab/tutorials/getting-started/#app-run
App.run(user_loop=loop)
