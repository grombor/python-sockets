import json
from server_files.server_config import USERS_FILEPATH
from server_files.user import UserAccountClass


class Authenticate:

    _users = []


    def login(self, login, password):
        """ Checks user credentials"""
        self.read_from_file()
        for _user in self._users:
            if (_user.get_username() == login) and (_user.get_password() == password):
                print(f"user from auth: {_user}")
                return _user
        return None


    def read_from_file(self):
        """ Reads from file list of users """
        try:
            with open(USERS_FILEPATH, "r") as f:
                users = json.loads(f.read())
                f.close()

                for _user in users:
                    u = UserAccountClass(**_user)
                    self._users.append(u)
                return
        except Exception as e:
            print(e)


    def add_user(self, username:str, password:str, is_admin: bool = False):
        u = UserAccountClass(username, password, is_admin)
        self._users.append(u)
        return u.to_json()


    def save_to_file(self):
        """ Save JSON users database to a file. """
        with open(USERS_FILEPATH, "a") as f:
            temp = []
            for _user in self._users:
                temp.append(_user.to_json())
            f.write(str(temp))
            f.close()


# Authenticate().read_from_file()
#
# for user in Authenticate()._users:
#     print(user)

#     def save_to_file(self, users) -> None:
#         """ Save JSON users database to a file. """
#         with open(USERS_FILEPATH, "a") as f:
#             f.write(users)
#             f.close()
#
#
# def create_new_user(self, data) -> None:
#     """
#     Creates a new user instance.
#     arg1 (type str) - username
#     arg2 (type str) - password
#     arg3 (type bool) - takes False for low-level users, True for admins. Default = False
#     """
#     new_user = UserAccountClass("name", "password")
#     return self.wrap("-create_new_user")
#     # self.add_user(new_user)+
#
#
#     def add_user(self, user):
#         """ Opens file and reads context from file. If file is not exist - creates a blank one. """
#         # Checks is file exist, if not creates a blank file
#         global users
#         # Append new user if not exist
#         users.append(user)
#         dict_to_json = {
#             "users": users
#         }
#         users = json.dumps(dict_to_json)
#         # Save to file
#         self.save_to_file(users)
#         # Close file
#
#
#     def is_admin(self, user):
#         credentials = user.split('@')
#         users = self.read_from_file()
#         for user in users:
#             if user['username'] == credentials[0] and user['password'] == credentials[1]:
#                 if user['is_admin']:
#                     return True