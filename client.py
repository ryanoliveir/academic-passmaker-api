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
    print('Welcome to P A S S  M A K E R !\n\n')


def view_all_services():
    
    print("Viewing all services...")
    input()
    # Add your logic to display all services

def add_new_service():
    print("Adding a new service...")
    input()
    # Add your logic to add a new service

def update_service():
    print("Updating a service...")
    input()
    # Add your logic to update a service

def remove_service():
    print("Removing a service...")
    input()
    # Add your logic to remove a service

def print_menu():
    for index, menu_option in enumerate(menu_options, start=1):
        print(f"({index}) {menu_option}")

def menu():
    try:
        choice = int(input("Enter your choice (1-4): "))
        return choice
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None



def home():
    while True:
        clear();
        print_menu()
        option = menu()

        if option == 1:
            view_all_services()
        elif option == 2:
            add_new_service()
        elif option == 3:
            update_service()
        elif option == 4:
            remove_service()
        else:
            print("Invalid option. Please choose a valid option. (Enter to continue)")
            input()
        


def login():
    
    email_input = input("Enter email: ")
    password_input = pwinput.pwinput(prompt="Enter password: ", mask='*')

    paylaod = { "email": email_input, "password": password_input}

    account = client.signIn(paylaod, '/login')

    if(account):
        clear()
        return home()
    else: 
        clear()
        login()



# fazer o codigo main aqui 

if __name__ == '__main__':
    clear()

    login()

   