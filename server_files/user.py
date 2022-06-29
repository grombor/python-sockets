from abc import ABC, abstractmethod


class AccountClass(ABC):
    """ Abstract account class interface. """

    @abstractmethod
    def __init__(self):
        """ Init method. """
        pass

    @abstractmethod
    def get_acc_name(self):
        """ Getter of account name. """
        pass

    @abstractmethod
    def set_acc_name(self):
        """ Setter of account name. """
        pass

    @abstractmethod
    def set_acc_name(self):
        """ Setter of account name. """
        pass

    @abstractmethod
    def get_is_admin(self):
        """ Getter of is_admin  attribute. """
        pass


class UserAccountClass(AccountClass):
    """ User account class. """

    messages = list()

    def __init__(self, acc_name: str, acc_pass: str, is_admin: bool = False):
        """ Init method. """
        self.acc_name = acc_name
        self.acc_pass = acc_pass
        self.is_admin = is_admin


    def get_acc_name(self):
        """ Getter of account name. """
        return self.acc_name


    def set_acc_name(self, name):
        """ Setter of account name. """
        self.acc_name = name


    def get_is_admin(self):
        """ Getter of is_admin  attribute. """
        return self.is_admin
