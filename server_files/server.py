import json
from datetime import datetime

from server_files.server_config import *
from server_files.user import UserAccountClass

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


    # TODO: change id, msg, cmd, is admin to User object
    def wrap(self, msg: str, id='server', cmd=None, is_admin=False) -> bytes:
        """ Takes string, insert into JSON format and encode it. Makes message ready to send. """
        text = {
            "id": id,
            "message": msg,
            "is_admin": is_admin,
            "cmd": cmd
        }
        message = json.dumps(text).encode(CODING)
        return message


    def start(self):
        """ Starts server. """
        print(self.greetings())


    def get_commands(self):
        """ Returns list of commands. """
        keys = self._commands.keys()
        return keys


    def stop(self):
        """ Shuts down a server. """
        return self.wrap("Shutting down a server.", cmd="-stop", is_admin=True)



    def show_help(self) -> str:
        """ Shows detailed list of commands. """
        text = "\n"
        for key, value in self._commands.items():
            text += f"{key}: {value} \n"
        return str(text)


    def show_version(self):
        """ Shows current server version. """
        return self.wrap(f"Current version of the server: {VERSION}")


    def show_uptime(self):
        """ Shows current server uptime. """
        uptime = str(datetime.now() - UPTIME)[:-7]
        return self.wrap(f"Server is online since {uptime} seconds.")


    def read_from_file(self):
        """ Reads from file list of users """
        try:
            with open(r'users.txt', "rt") as file:
                context = file.read()
                print(context)
                return context
        except FileNotFoundError as e:
            with open(r'users.txt', "x") as f:
                f.close()


    def add_user(self, user):
        """ Opens file and reads context from file. If file is not exist - creates a blank one. """
        users = self.read_from_file()
        # Append new user if not exist
        if user not in users:
            users.append(user)
        # Save to file
        # Close file
        pass


    def create_user(selfself, name, password):
        """
        Creates a new user instance.
        arg1 (type str) - username
        arg2 (type str) - password
        arg3 (type bool) - False for normal users, True for admins. Default = False
        """
        return UserAccountClass(name, password)


    def login(self):
        """ Sends back client login request. """
        return self.wrap("-login")


    def handle_commands(self, command):
        """ Flow control of server commands. """
        match command:
            case '-quit' | '-stop':
                return self.stop()
            case '-help':
                return self.show_help()
            case '-info':
                return self.show_version()
            case '-uptime':
                return self.show_uptime()
            case '-login':
                return self.login()
            case _:
                print("other")


