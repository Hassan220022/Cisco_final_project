import socket  # Import the socket module for networking
import signal  # Import the signal module for handling signals
import sys  # Import the sys module for system-related operations
import threading  # Import the threading module for creating threads

HOST = socket.gethostname()  # Get the hostname of the local machine
PORT = 8888  # Define the port number to use

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(
    f"Socket created on host: {HOST}"
)  # Print a message indicating the socket creation

try:
    # Bind the socket to the specified host and port
    server_socket.bind((HOST, PORT))
except socket.error as msg:
    # If binding fails, print an error message and exit
    print(f"Bind failed. Error Code: {str(msg[0])} Message: {msg[1].decode()}")
    sys.exit()

print("Socket bind complete")  # Print a message indicating successful binding
print("Socket now listening")  # Print a message indicating the socket is listening


# Define a signal handler function to handle SIGINT (Ctrl+C)
def signal_handler(sig, frame):
    print("Shutting down server...")  # Print a message indicating server shutdown
    server_socket.close()  # Close the server socket
    sys.exit(0)  # Exit the program


# Register the signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)


# Define a function to handle client connections
def handle_client(data, addr):
    received_data = data.decode()  # Decode the received data
    print(
        f"Received from {addr}: {received_data}"
    )  # Print the received data and client address
    reversed_data = received_data[::-1]  # Reverse the received data
    reply = bytes(reversed_data, "utf-8")  # Encode the reversed data into bytes
    server_socket.sendto(reply, addr)  # Send the reversed data back to the client
    print(
        f"Sent to {addr}: {reversed_data}"
    )  # Print the reversed data and client address


print(
    "Waiting to receive messages..."
)  # Print a message indicating waiting for messages

while True:
    # Receive data from a client
    data, addr = server_socket.recvfrom(1024)
    # Create a new thread to handle the client connection
    client_thread = threading.Thread(target=handle_client, args=(data, addr))
    client_thread.start()  # Start the new thread
