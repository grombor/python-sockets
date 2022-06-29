import json
import socket
from server_files.server import Server
from server_files.server_config import *

# print("Starting server...")
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen(5)
#     client_socket, client_address = s.accept()
#     with client_socket:
#         print(f"connected {client_address}")
#         while True:
#             data = client_socket.recv(HEADER_SIZE).decode(CODING)
#             if not data:
#                 print("terminating connection")
#                 client_socket.close()
#                 break
#             message = json.loads(data)
#             print(f"message1: {message}")
#             command = message['message']
#             print(f"message2: {message}")
#             if command in Server().get_commands():
#                 msg = Server().handle_commands(command)
#                 print(f"send command {msg}")
#                 client_socket.send(msg)
#             else:
#                 msg = "Unknown command. Type '-help' for more info.".encode(CODING)
#                 client_socket.send(msg)

Server().read_from_file()

