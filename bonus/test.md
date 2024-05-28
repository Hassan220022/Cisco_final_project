# Test Cases and Execution Traces

## Test Cases

1. TCP Connection with Remote Host:
   - Run the TCP server on a remote host (or a different machine on the same network).
   - Run the TCP client and enter the remote host's IP address or hostname.
   - Enter a string to reverse on the client.
   - Verify that the reversed string is received and displayed correctly.
   - Enter 'exit' to quit the client.
   - Verify that the client and server terminate gracefully.

2. UDP Connection with Remote Host:
   - Run the UDP server on a remote host (or a different machine on the same network).
   - Run the UDP client and enter the remote host's IP address or hostname.
   - Enter a string to reverse on the client.
   - Verify that the reversed string is received and displayed correctly.
   - Enter 'exit' to quit the client.
   - Verify that the client and server terminate gracefully.

## Execution Traces

### Test Case 1: TCP Connection with Remote Host

```bash
Server:
$ python .\server_tcp.py
Socket created on host: 192.168.1.28
Socket bind complete
IP address:  O-Laptop.local
Socket now listening
Connected with 192.168.1.39:59500
omar
ramo

Client:
PS C:\Users\mohab\OneDrive\Desktop> python .\client.py
Enter Server Host Ip/name: 192.168.1.28
Connecting to ('192.168.1.28', 8888)...
Connected to server
Enter a string to reverse (or "exit" to quit): omar
Sending: omar
Received: ramo

Enter a string to reverse (or "exit" to quit):
```

### Test Case 2: UDP Connection with Remote Host

```bash
server:

Socket created on host: 192.168.1.80
Socket bind complete
Socket now listening
Waiting to receive messages...
Received from ('192.168.1.250', 64503): mikawi
Sent to ('192.168.1.250', 64503): iwakim
Received from ('192.168.1.250', 64503): bor3i
Sent to ('192.168.1.250', 64503): i3rob
Received from ('192.168.1.250', 64503): omar
Sent to ('192.168.1.250', 64503): ramo
Received from ('192.168.1.250', 64503): ahmed
Sent to ('192.168.1.250', 64503): demha
Received from ('192.168.1.250', 64503): anwar
Sent to ('192.168.1.250', 64503): rawna

client:

Enter Server Host Ip/name: 192.168.1.80
Connecting to ('192.168.1.80', 8888)...
Enter a string to reverse (or "exit" to quit): mikawi
Sending: mikawi
Received: iwakim
Enter a string to reverse (or "exit" to quit): bor3i
Sending: bor3i
Received: i3rob
Enter a string to reverse (or "exit" to quit): omar
Sending: omar
Received: ramo
Enter a string to reverse (or "exit" to quit): ahmed
Sending: ahmed
Received: demha
Enter a string to reverse (or "exit" to quit): anwar
Sending: anwar
Received: rawna
Enter a string to reverse (or "exit" to quit):
```

Known Issues:

- The program does not handle network errors or disconnections gracefully. It may terminate abruptly in such cases.
- The program does not perform any input validation or sanitization, which may lead to security vulnerabilities or unexpected behavior.
