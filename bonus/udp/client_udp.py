import socket  # Import the socket module for networking

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a UDP socket

# Get server hostname or IP address
server_hostname = "mikawi.duckdns.org"  # Get the server hostname or IP address
port = 888  # Define the port number to use

# Set the server address
server_address = (
    server_hostname,
    port,
)  # Create a tuple with the server address and port
print(
    f"Connecting to {server_address}..."
)  # Print a message indicating the connection attempt

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
        client_socket.sendto(message, server_address)  # Send the message to the server

        # Receive the response from the server
        data, server = client_socket.recvfrom(1024)  # Receive the response from the server
        received_data = data.decode()  # Decode the received data
        print(f"Received: {received_data}")  # Print the received response

except Exception as e:
    print(
        f"Error sending or receiving data: {e}"
    )  # Print an error message if an exception occurs

finally:
    client_socket.close()  # Close the client socket
    print("Connection closed")  # Print a message indicating the connection is closed
