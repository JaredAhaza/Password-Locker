import pyperclip
import random
import string

class Credentials:

    credentials_list = [] #empyt credentials array
    """
    Generates new instatce of credentials
    """

    def __init__(self,site,username,password):
        """
        Args:
        site:new credential in a site
        username:new credential user in the site
        password:new credential password in the site
        """

        self.site = site
        self.username = username
        self.password = password

    def save_credentials(self):
        """
        saves credentials into the empty array
        """

        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        deletes credentials from the array
        """

        Credentials.credentials_list.remove(self)
    
    @classmethod
    def find_by_site(cls,site):
        """
        Method takes in the site and returns credentials matching it
        Args:
            site:site to search for

        Returns:
            credentials that matches the site
        """
        for credentials in cls.credentials_list:
            if credentials.site == site:
                return credentials


    @classmethod
    def credentials_exist(cls,site):
        """
        Method check if the credentials exist
        Args:
            site:login to search if it exists
        Returns:
            Boolean: true or false
        """
        for credentials in cls.credentials_list:
            if credentials.site == site:
                return True
                return False


    @classmethod
    def display_credentials(cls):
        """
        method returns existing credentials
        """
        return cls.credentials_list


    # @classmethod
    # def copy_password(cls,site):
    #     credentials_found = Credentials.find_by_site(site)
    #     pyperclip.copy(credentials_found.password)


    @classmethod
    def generate_password(cls, pass_length):
        """
        Method generatin password
        """
        allchar = string.ascii_letters + string.punctuation + string.digits
        password = ''.join(random.sample(allchar, int(pass_length)))
        return password




print("hi")

