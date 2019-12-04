class User:

    def __init__(self, email, name, last_name):
        self.__email = email
        self.__name = name
        self.__last_name = last_name

    @property
    def email(self):
        return self.__email

    @property
    def name(self):
        return self.__name

    @property
    def last_name(self):
        return self.__last_name