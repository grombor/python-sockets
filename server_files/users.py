class Users:

    _clients = list()

    _admins = [
        "arek",
    ]

    def add_user(self, client):
        """ Add a client to the list"""
        self._clients.append(client)


    def add_admin(self, nickname):
        """ Add an admin to the list"""
        self._admins.append(nickname)

    def get_admins(self):
        return self._admins

