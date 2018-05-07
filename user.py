class User:
    """
    class generating new instances of users
    """

    counter = 0
    users = dict()

    def __init__(self,login_password):

        self.username = username
        self.login_password = login_password
        User.users = {"username":self.username,"password":self.login_password}
        User.counter+=1

    # @classmethod    
    # def number_of_users(cls):
    #     return f"There are these {cls} user(s)"
    @classmethod
    def list_users(cls):
        return cls.users






