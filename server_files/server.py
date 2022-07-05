import json
from datetime import datetime

from server_files.server_config import *
from server_files.auth import Authenticate
from server_files.user import logged_in_user

_logged_in_user = logged_in_user


class Server:
    """
    Server class is responsible for the operation of the server.
    """

    _user = None


    _commands = {
        "-quit": "stop server and client",
        "-stop": "stop server and client",
        "-help": "show this help",
        "-info": "show server version and creation date",
        "-uptime": "show server lifetime",
        "-create_user": "creates a new user",
        "-login": "send user credentials to log in"
    }


    def greetings(self):
        """ Shows greetings. """
        return f".:: Welcome to the {HOST} server! Type '--help' for info. ::.\n"


    def wrap(self, msg: str, data: str ="", id: str ='server') -> bytes:
        """ Takes string, insert into JSON format and encode it. Makes message ready to send. """
        text = {
            "id": id,
            "message": msg,
            "data": data
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
        return self.wrap("-stop")



    def show_help(self) -> str:
        """ Shows detailed list of commands. """
        text = "\n"
        for key, value in self._commands.items():
            text += f"{key}: {value} \n"
        return self.wrap(text)


    def show_version(self):
        """ Shows current server version. """
        return self.wrap(f"Current version of the server: {VERSION}")


    def show_uptime(self):
        """ Shows current server uptime. """
        uptime = str(datetime.now() - UPTIME)[:-7]
        return self.wrap(f"Server is online since {uptime} seconds.")


    def handle_commands(self, message, data):
        """ Flow control of server commands. """
        match message:
            case '-quit' | '-stop':
                return self.stop()
            case '-help':
                return self.show_help()
            case '-info':
                return self.show_version()
            case '-uptime':
                return self.show_uptime()
            case '-create_user':
                # New user logic
                global _logged_in_user
                if _logged_in_user.get_is_admin():
                    if data:
                        # Create new user
                        print(f"{data=}")
                        credentials = data.split('@')
                        Authenticate().add_user(*credentials)
                        Authenticate().save_to_file()
                        return self.wrap("User created successfully.")
                    return self.wrap("-login", "")
                else: return self.wrap("Only Admin can create new users.")
            case '-login':
                # Login in logic
                credentials = data.split('@')
                self._user = Authenticate().login(*credentials)
                _logged_in_user = self._user
                if self._user is not None:
                    data = "user"
                    if self._user.get_is_admin():
                        data = "admin"
                    return self.wrap("OK", data)
                else: self.wrap("NOT OK")
            case _:
                print("other")


