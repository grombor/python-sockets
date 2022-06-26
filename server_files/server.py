import json
import socket

from server_files.server_config import *

class Server:
    """
    Server class is responsible for the operation of the server.
    """


    _commands = {
        "-quit": "stop server and client",
        "-stop": "stop server and client",
        "-help": "show this help",
        "-info": "show server version and creation date",
        "-uptime": "show server lifetime",
    }


    def greetings(self):
        """ Shows greetings. """
        return f".:: Welcome to the {HOST} server! Type '--help' for info. ::.\n"


    def wrap(self, msg: str) -> bytes:
        """ Takes string, insert into JSON format and encode it. Makes message ready to send. """
        text = {
            "id": "server",
            "message": msg
        }
        message = json.dumps(text).encode(CODING)
        return message


    def start(self):
        """ Starts server """
        # Show greetings
        print(self.greetings())


    def get_commands(self):
        keys = self._commands.keys()
        return keys


    def show_help(self) -> str:
        text = "\n"
        for key, value in self._commands.items():
            text += f"{key}: {value} \n"
        return str(text)


    def handle_commands(self, command):
        match command:
            case '-quit':
                print("-quit")
            case '-stop':
                print("-stop")
            case '-help':
                return self.wrap(self.show_help())
            case '-info':
                print("-info")
            case '-uptime':
                print("--uptime")
            case '-login':
                print("-login")
            case _:
                print("other")


