import socket  # Import the socket module for networking
import sys  # Import the sys module for system-related operations
import threading  # Import the threading module for creating threads
import signal  # Import the signal module for handling signals

HOST = socket.gethostname()  # Get the hostname of the local machine
PORT = 8888  # Define the port number to use

# Create a TCP socket (SOCK_STREAM for TCP, SOCK_DGRAM for UDP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
server_socket.listen(10)  # Listen for incoming connections (backlog=10)
print("Socket now listening")  # Print a message indicating the socket is listening


# Define a signal handler function to handle SIGINT (Ctrl+C)
def signal_handler(sig, frame):
    print("Shutting down server...")  # Print a message indicating server shutdown
    server_socket.close()  # Close the server socket
    sys.exit(0)  # Exit the program


# Register the signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)


# Function for handling client connections
def clientthread(conn):
    # conn.send(b'Welcome to the server. Receiving Data...\n')  # Uncomment to send a welcome message
    while True:
        # Receive data from the client
        data = conn.recv(1024)
        if not data:
            break  # Exit the loop if no data is received
        received_data = data.decode()  # Decode the received data
        print(received_data)  # Print the received data
        reversed_data = received_data[::-1]  # Reverse the received data
        reply = (
            bytes(reversed_data, "utf-8") + b"\n"
        )  # Encode the reversed data into bytes and add a newline
        conn.sendall(reply)  # Send the reversed data back to the client
    conn.close()  # Close the client connection


# Keep accepting connections
while True:
    try:
        conn, addr = server_socket.accept()  # Accept a new connection
        print(f"Connected with {addr[0]}:{str(addr[1])}")  # Print the client's address
        client_thread = threading.Thread(
            target=clientthread, args=(conn,)
        )  # Create a new thread for the client
        client_thread.start()  # Start the new thread
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        signal_handler(signal.SIGINT, None)
