import json
import socket
from server_files.server import Server
from server_files.server_config import *

print("Starting server...")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    client_socket, client_address = s.accept()
    with client_socket:
        print(f"connected {client_address}")
        while True:
            # Receive data from client
            data = client_socket.recv(HEADER_SIZE).decode(CODING)

            # If receive no response or null response from client
            # ex. client fatal error. Then turn server off.
            if data is None:
                print(f"terminating connection, received {data=}")
                client_socket.close()
                break

            # Converts client message from JSON to <dict>
            message = json.loads(data)
            print(f"received message: {message}")

            # Checks is message from client is a server command
            if message['message'] in Server().get_commands():
                msg = Server().handle_commands(**message)
                client_socket.send(msg)
                continue
            # If message is not a server command send tooltip to client
            else:
                # message is not None:
                client_socket.send(Server().unknown_command())



