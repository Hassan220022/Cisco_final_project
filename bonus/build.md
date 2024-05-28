# Building and Executing the Program

Requirements:

- Python 3.x installed on your system

Building the Program:
No building process is required as the program is written in Python, an interpreted language.

Executing the Program:

1. TCP Server:
   - Navigate to the 'tcp' folder in the repository.
   - Run the following command to start the TCP server:
     python server.py

2. TCP Client:
   - Navigate to the 'tcp' folder in the repository.
   - Run the following command to start the TCP client:
     python client.py
   - Follow the prompts to connect to the server and enter strings to reverse or 'exit' to quit.

3. UDP Server:
   - Navigate to the 'udp' folder in the repository.
   - Run the following command to start the UDP server:
     python server.py

4. UDP Client:
   - Navigate to the 'udp' folder in the repository.
   - Run the following command to start the UDP client:
     python client.py
   - Follow the prompts to enter the server's host IP/name and strings to reverse or 'exit' to quit.

Note:

- Make sure to run the server before running the client.
- For the TCP client, you may need to enter the server's IP address or hostname if running on different machines.
- For the UDP client, you will be prompted to enter the server's host IP/name.
- Press 'Ctrl+C' to gracefully terminate the server or client processes.
