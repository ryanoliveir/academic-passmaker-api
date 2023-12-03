from model.client import Client
from getpass import getpass
import pwinput
from os import system
# classe para pegar e mandar dados para a api
client = Client('http://localhost:5000', '/api' )



#clarar outras funções aqui

menu_options = [
    "View all services",
    "Add new serrvice",
    "Update service",
    "Remove service"
]


def clear():
    system("cls || clear")


def login():
    clear()
    
    email_input = input("Enter email: ")
    password_input = pwinput.pwinput(prompt="Enter password: ", mask='*')

    paylaod = { "email": email_input, "password": password_input}

    account = client.signIn(paylaod, '/login')

    if(account):
        return home()
    else: 
        login()



def menu():

    for  index, menu_option in enumerate(menu_options):
        print(f"({index + 1}) {menu_option}")


def home():
    menu()    


# fazer o codigo main aqui 

if __name__ == '__main__':
    print('Welcome to PassMaker !')

    login()

   