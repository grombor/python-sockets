import socket
import json
from client_files.config import *
from client_files.client import Client

c = Client()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to server
    s.connect((HOST, PORT))

    # Login loop
    while True:
        # Send login@passowrd
        s.send(c.wrap(*c.login()))
        # Shows client's greetings after successful connection
        request = json.loads(s.recv(HEADER_SIZE).decode(CODING))
        if request['message'] == "OK":
            if request['data'] == "admin":
                is_admin = True
            break

    # Sends greeting after successfully login
    c.greetings()
    # Take text of the message text form keyboard input
    message = c.get_message()
    # Wraps a message to JSON format and sends it to server
    s.send(c.wrap(message))
    while True:
        try:
            # Receives a message from server and unwrap it to dict
            request = json.loads(s.recv(HEADER_SIZE).decode(CODING))
            message = request['message']
            data = request['data']
        except Exception as e:
            s.close()
            print(f"Something went wrong: {e}")

        if c.is_command(message):
            match message:
                case "-stop" | "-quit":
                    print("Quitting")
                    s.close()
                    break
                case "-login":
                    message, data = c.login()
                    message = "-create_user"
                    s.send(c.wrap(message, data))
                    print("Press Enter to confirm.")
                case _:
                    print("Unknown command")
        else:
            print(f'message received: {message}')

        # Take text of the message text form keyboard input
        message = c.get_message()
        # Wraps a message to JSON format and sends it to server
        s.send(c.wrap(message))
        print(f"message sended: {message}")

