import socket  # Import the socket module for networking

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get server hostname or IP address
server_hostname = input("Enter Server Host Ip/name: ")  # Get the server hostname or IP address
port = 8888  # Define the port number to use
# Connect to the server
server_address = (
    server_hostname,
    port,
)  # Create a tuple with the server address and port
print(
    f"Connecting to {server_address}..."
)  # Print a message indicating the connection attempt
try:
    client_socket.connect(server_address)  # Attempt to connect to the server
except Exception as e:
    print(
        f"Error connecting to server: {e}"
    )  # Print an error message if the connection fails
    exit(1)  # Exit the program with an error code

print("Connected to server")  # Print a message indicating successful connection

try:
    while True:
        # Get input from the user
        message = input(
            'Enter a string to reverse (or "exit" to quit): '
        ).encode()  # Get user input and encode it

        # Check if the user wants to exit
        if (
            message.decode().lower() == "exit"
        ):  # Check if the user entered 'exit' (case-insensitive)
            break  # Exit the loop if 'exit' is entered

        # Send the message to the server
        print(f"Sending: {message.decode()}")  # Print the message being sent
        client_socket.sendall(message)  # Send the message to the server

        # Receive the response from the server
        data = client_socket.recv(1024)  # Receive the response from the server
        print(f"Received: {data.decode()}")  # Print the received response

except Exception as e:
    print(
        f"Error sending or receiving data: {e}"
    )  # Print an error message if an exception occurs

finally:
    # Clean up the connection
    client_socket.close()  # Close the client socket
    print("Connection closed")  # Print a message indicating the connection is closed
