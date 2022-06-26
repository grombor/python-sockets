""" User class """
import json

from client_files.config import *


class User:
    """ User class nad methods """


    # Variables
    nickname = ""
    message = ""

    def get_nickname(self) -> str:
        """ Get nickname from user. """
        try:
            self.nickname = input("Enter nickname: ")
            return self.nickname
        except RuntimeError as re:
            print(re)


    def login(self):
        """ Printing welcome message."""
        self.nickname = self.get_nickname()
        print(f"Hello {self.nickname}!")
        print(f"Logining in to {HOST}...")


    def send_message(self):
        """ Send message to server function. """

        self.message = input("Command: ")
        msg = {
            "nickname": self.nickname,
            "message": self.message
        }
        msg_to_send = json.dumps(msg).encode(CODING)
        return msg_to_send
