import sys
import time
import string
import random
from user import User
from password import Credentials

def login():
    """
    Method that handles login capabilities of a user
    """
    if User.users:
        username = input("Enter username")
        pasword = input ("Enter your password")
        if User.username['username'] == username and User.login_password['password'] == pasword:
            print(f"welcome, {username}")

    else:
        print("wrong password or username")
        print("choose an option: \n 1)register \n 2)Try again")
        data = int(input())

        if data == 1:
            register()
        elif data == 2:
            login()
        else:
            print("There are no such users, please register")
            register()

def register():
    """
    Allows registration to be done by entering the username and password
    """
    username = input("enter username")
    password1 = input("enter password")
    password2 = input("re-enter password")
    if password1 == password2:
        User(username,password1)
        return True
    else:
        register()
        landing_section = True

def addAccount():
    """
    Enables addition of credentials
    """

    acc = input("enter your account name")
    username = ("choose a username")
    email = ("enter emeil address")
    password = int(input("Enter your password"))
    Credentials(acc,username,email,generate_password(password))

def generate_password(i):
    _all = string.ascii_letters+ string.punctuation+string.digits
    return "".join(random.sample(_all,i))


def viewall():
    """
    function allows for viewing all the accounts the user has
    """
    print(Credential.display_accounts())


def delete_account():
    """
    function to delete an account and the user has to indicate the account to be deleted
    """
    Credential.delete_credential(input("Indicate account to be deleted"))

def search_account():
    """
    Function to search an account
    """

    acc = input ("which account are you searching for ? ")
    screen(Creddential.search_credential(acc))

def landing_section():
    """
    allows the user to specify whether to login, reister or leave the app
    """

    selecting = True
    while selecting:
        """
        loops until login or register function returns True
        """
        input_ = int(input("1:login,2:register,3:leave"))

        if input_ == 1:
            return login()

        elif input_ == 2:
            return register()

        elif input_ ==3:
            screen("Thanks for comming here, application is closing")

        else:
            screen("Invalid choice! Try again")

    def main():
        """
        landing section is called here and if return value is true password locker options are unlocked
        """
        screen("Hello")
        decided = landing_section

    if decided:
        screen("you are now logged in to the password locker!")
        logedin = True

    while logedin:
        choice = int(input("1)create account\n2)view all accounts\n3)delete account\n4)search account\n5)logout"))
    if choice == 1:
        '''
        option to create an account
        '''
        print("you want to create a new account")
        addAccount()
    elif choice == 2:
        '''
        option to view all the accounts
        '''
        print("view all the accounts")
        viewall()

    elif choice == 3:
        '''
        option to delete an account
        '''
        print("delete an account")
        delete_account()

    elif choice == 4:
        '''
        option to search an account
        '''
        print("search account")
        search_account()

    elif choice == 5:
        '''
        option to log out
        '''
        print("log out")

        loggedin = False
        print("bye, thank you for using this app")

    else:
        print("bye")


if __name__ == '__main__':
    landing_section()