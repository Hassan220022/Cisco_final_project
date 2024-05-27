# Test Cases and Execution Traces

Test Cases:

1. TCP Connection:
   - Run the TCP server and client on the same machine.
   - Enter a string to reverse on the client.
   - Verify that the reversed string is received and displayed correctly.
   - Enter 'exit' to quit the client.
   - Verify that the client and server terminate gracefully.

2. TCP Connection with Remote Host:
   - Run the TCP server on a remote host (or a different machine on the same network).
   - Run the TCP client and enter the remote host's IP address or hostname.
   - Enter a string to reverse on the client.
   - Verify that the reversed string is received and displayed correctly.
   - Enter 'exit' to quit the client.
   - Verify that the client and server terminate gracefully.

3. UDP Connection:
   - Run the UDP server and client on the same machine.
   - Enter the server's host IP/name on the client.
   - Enter a string to reverse on the client.
   - Verify that the reversed string is received and displayed correctly.
   - Enter 'exit' to quit the client.
   - Verify that the client and server terminate gracefully.

4. UDP Connection with Remote Host:
   - Run the UDP server on a remote host (or a different machine on the same network).
   - Run the UDP client and enter the remote host's IP address or hostname.
   - Enter a string to reverse on the client.
   - Verify that the reversed string is received and displayed correctly.
   - Enter 'exit' to quit the client.
   - Verify that the client and server terminate gracefully.

5. Invalid Input:
   - Run the TCP or UDP client.
   - Enter an invalid string (e.g., containing non-ASCII characters) on the client.
   - Verify that the program handles the invalid input gracefully without crashing.

Execution Traces:
[Attach execution traces showing the test cases being run.]

Known Issues:

- The program does not handle network errors or disconnections gracefully. It may terminate abruptly in such cases.
- The program does not perform any input validation or sanitization, which may lead to security vulnerabilities or unexpected behavior.
