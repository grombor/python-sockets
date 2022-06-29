import socket
import json
from client_files.config import *
from client_files.client import Client

c = Client()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # Shows client's greetings after successful connection
    c.greetings()
    # Gets message text form keyboard input
    message = c.get_message()
    # Wraps a message to JSON format and sends it to server
    s.send(c.wrap(message))
    print(f"message sended: {message}")
    # Receives a message from server and unwrap it to dict
    # raw_data = s.recv(HEADER_SIZE).decode(CODING)
    data = json.loads(s.recv(HEADER_SIZE).decode(CODING))
    # print(raw_data)
    # data = json.loads(raw_data)
    message = data['message']
    cmd = data['cmd']
    if cmd == "stop":
        print("Quitting")
    # Prints message in console
    # print(f"message recived: {message}")

