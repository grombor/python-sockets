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
        if self.find_user_by_name(username) is None:
            self._users.append(u)
            self.save_to_file()
            return u.to_json()
        return None


    def save_to_file(self):
        """ Save JSON users database to a file. """
        with open(USERS_FILEPATH, "w") as f:
            temp = []
            for _user in self._users:
                temp.append(_user.to_json())
            f.write(json.dumps(temp))
            f.close()


    def find_user_by_name(self, username):
        """ Search users database by a username. If username is found, return the user object, else return false"""
        for _user in self._users:
            if _user.get_username == username:
                return _user
            return None


    def remove_user(self, username):
        """ Removes a user """
        _user = self.find_user_by_name(username)
        if _user is None:
            return None
        else:
            self._users.remove(_user)
            self.save_to_file()
            return True


    def edit_user(self, data):
        """ Edits a user """
        username, new_username, new_password, is_admin = data.split('@')
        _user = self.find_user_by_name(username)
        if _user is None:
            return None
        else:
            _user.set_usename(new_username)
            _user.set_password(new_password)
            _user.set_is_admin(is_admin)
            self.save_to_file()
            return True

