# Socket Programming Bonus Task

This repository contains examples of socket programming using Python. It includes implementations for both TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) connections, with separate folders for each protocol.

## Folder Structure

```plaintext
├── README.md
├── tcp/
│   ├── client_tcp.py
│   └── server_tcp.py
└── udp/
    ├── client_udp.py
    └── server_udp.py
```

## TCP (Transmission Control Protocol)

The `tcp` folder contains the implementation of a TCP client and server.

### Server TCP

`server_tcp.py` is a Python script that creates a TCP server. It listens for incoming connections on a specified host and port. When a client connects, the server receives data from the client, reverses the data, and sends it back to the client.

To run the server, execute the following command:

```bash
python server_tcp.py
```

### Client TCP

`client_tcp.py` is a Python script that creates a TCP client. It connects to the server and allows the user to send strings to the server. The server will reverse the string and send it back to the client.

To run the client, execute the following command:

```bash
python client_tcp.py
```

The client will prompt you to enter a string to reverse or 'exit' to quit the program.

## UDP (User Datagram Protocol)

The `udp` folder contains the implementation of a UDP client and server.

### Server UDP

`server_udp.py` is a Python script that creates a UDP server. It listens for incoming messages on a specified host and port. When a message is received from a client, the server reverses the message and sends it back to the client.

To run the server, execute the following command:

```bash
python server_udp.py
```

### Client UDP

`client_udp.py` is a Python script that creates a UDP client. It allows the user to send strings to the server. The server will reverse the string and send it back to the client.

To run the client, execute the following command:

```bash
python client_udp.py
```

The client will prompt you to enter the server host IP/name and then a string to reverse or 'exit' to quit the program.

## Requirements

- Python 3.x
