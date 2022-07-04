import socket
import json
from client_files.config import *
from client_files.client import Client

c = Client()
is_admin = None

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to server
    s.connect((HOST, PORT))

    while True:
        # TODO: Make Object - User with id and pass
        # Send login@passowrd
        s.send(c.wrap(*c.login()))
        # Shows client's greetings after successful connection
        request = json.loads(s.recv(HEADER_SIZE).decode(CODING))
        if request['message'] == "OK":
            break

    # Sends greeting after successfully login
    c.greetings()
    # Take text of the message text form keyboard input
    message = c.get_message()
    # Wraps a message to JSON format and sends it to server
    s.send(c.wrap(message))
    while True:
        # Receives a message from server and unwrap it to dict
        request = json.loads(s.recv(HEADER_SIZE).decode(CODING))
        message = request['message']
        data = request['data']

        if c.is_command(message):
            match message:
                case "-stop" | "-quit":
                    print("Quitting")
                    s.close()
                    break
                case "-is_admin":
                    message = "is admin!"
                    print(message)
                    s.send(message)
        else:
            print(f'message received: {message}')

        # Take text of the message text form keyboard input
        message = c.get_message()
        # Wraps a message to JSON format and sends it to server
        s.send(c.wrap(message))
        print(f"message sended: {message}")

