import json
from datetime import datetime

from server_files.server_config import *
from server_files.admin import Admin
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
        "-messagebox": "checks offline messages in messagebox",
        "-create_user": "creates a new user - admin only",
        "-edit_user": "updates user data - admin only",
        "-remove_user": "removes a user - admin only",
        "-send": "sends a message to user",
        "-new_user": "should be hidden",
        "-login": "should be hidden",
        "-update_user": "should be hidden"
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


    def send_msg_to_user(self, data):
        """ Finds user in a userlist,
        if user exists, adds a new offline message"""
        username, message = data.split('@')
        a = Admin()
        a.read_from_file()
        user = a.find_user_by_name(username)
        if user is None:
            return self.wrap("User does not exists.")
        else:
            user.set_message(message)
            a.save_to_file()
            return self.wrap("The message sent.")

    def unknown_command(self):
        return self.wrap("Unknown command. Type '-help' for more info.")


    def handle_commands(self, message, data):
        """ Flow control of server commands. """
        # Checks is user logged in
        global _logged_in_user

        match message:
            case "-quit" | "-stop":
                return self.stop()
            case "-help":
                return self.show_help()
            case "-info":
                return self.show_version()
            case "-uptime":
                return self.show_uptime()
            case "-create_user":
                # Checks user is an admin
                if _logged_in_user.get_is_admin():
                    return self.wrap("-new_user")
                else: return self.wrap("Only Admin can create new users.")
            case "-new_user":
                if data:
                    # Create new user
                    credentials = data.split('@')
                    if credentials[2] == "False":
                        credentials[2] = False
                    if Admin().add_user(*credentials) is not None:
                        return self.wrap("User created successfully.")
                    return self.wrap("The user already exists.")
                return self.wrap("Error: no data")
            case "-edit_user":
                # Checks user is an admin
                if _logged_in_user.get_is_admin():
                    return self.wrap("-update_user")
                else:
                    return self.wrap("Only Admin can create new users.")
            case "-update_user":
                if Admin().edit_user(data):
                    return self.wrap("User edited successfully.")
                return self.wrap("User update failed.")
            case "-login":
                # Login in logic
                credentials = data.split('@')
                self._user = Admin().login(*credentials)
                _logged_in_user = self._user
                if self._user is not None:
                    try:
                        data = "user"
                        if self._user.get_is_admin():
                            data = "admin"
                        return self.wrap("OK", data)
                    except AttributeError:
                        return self.wrap("Error: Incorrect username or password")
                else: return self.wrap("Incorrect username or password")
            case "-remove_user":
                if Admin().remove_user(data):
                    return self.wrap("User deleted successfully.")
                return self.wrap("User does not exists.")
            case "-messagebox":
                messages = _logged_in_user.get_messages()
                print(f"user: {_logged_in_user=} and {self._user}, messages: {messages=}")
                if len(messages) > 0 :
                    return self.wrap(_logged_in_user.show_offline_messages())
                return self.wrap("You have no new messages")
            case "-send":
                if data == "":
                    return self.wrap("-send")
                else:
                    return self.send_msg_to_user(data)
            case _:
                print("Unknown command")


