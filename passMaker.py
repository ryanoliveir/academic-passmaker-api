from model.client import Client
from getpass import getpass
import pwinput
from os import system
import time

def colorprint(frase, color):
    if color == 'red':
        print('\033[91m',end="")
        print(frase,end="")
        print('\033[0m',end="")

    if color == 'green':
        print('\033[92m',end="")
        print(frase,end="")
        print('\033[0m',end="")

# classe para pegar e mandar dados para a api 
client = Client('http://localhost:5000', '/api' )

#clarar outras funções aqui
menu_options = [
    "View all services",
    "Add new service",
    "Remove service",
    "Update service"]

def clear():
    system("cls || clear\n")

def view_all_services(id_account):
    
    clear()
    print("All services")
    print("---------------------------------------------------------\n")
    current_services = client.getServices(f'/services/?id_account={id_account}')

    for service in current_services:
        print("")
        name_service = service['name']
        colorprint('Service: ', "green")
        print(name_service)
        
        email = service['userEmailService']
        print("Email: "+email)

        password = service['servicePassword']
        print("Password: "+password)
        
        url = service['site']
        print("Website Url: "+url)

    input("\n(1) return  ")

# FALTA IMPLEMENTAR!
def add_new_service(id_account):

    clear()
    print("Add New Service")
    print("---------------------------------------------------------\n")
    new_service_name = input("Insert Service Name: ")
    new_service_site = input("Insert Service Url: ")
    new_service_email = input("Insert Service Email: ")
    new_service_password = input("Insert Service Password: ")

    payload = {
        "account_id": int(id_account),
        "name": new_service_name,
        "site": new_service_site,
        "userEmailService": new_service_email,
        "servicePassword": new_service_password
    }

    response = client.createServices(payload, '/services/')

    # print(response)
    # input()

    print('\033[92m',end="")
    print("\nService added successfully!")
    print('\033[0m',end="")
    time.sleep(0.7)


def update_service(id_account):
    clear()
    print("Select the service to ",end="")
    colorprint("Update",'green')
    print("\n---------------------------------------------------------\n")
    current_services = client.getServices(f'/services/?id_account={id_account}')

    for service in current_services:
        print("")
        name_service = service['name']
        colorprint('Service: ', "green")
        print(name_service)
        
        email = service['userEmailService']
        print("Email: "+email)

        password = service['servicePassword']
        print("Password: "+password)
        
        url = service['site']
        print("Website Url: "+url)

        id = service['id_service']
        print("Service ",end ='')
        colorprint("ID", 'green')
        print(": "+ str(id))

    id_update = input("\nInsert the ID to update: ")

    for current_service in current_services: 
        if current_service['id_service'] == int(id_update):
            print("\nService found!\n")

            clear()
            print("Update Service")
            print("\n---------------------------------------------------------\n")
            new_name = input("Update Service name: ")
            new_email = input("Update Service email: ")
            new_password = input("Update Service password: ")
            new_url = input("Update Service website URL: ")

            updated_service = {
                'name': new_name,
                'userEmailService': new_email,
                'servicePassword': new_password,
                'site': new_url
            }

            updated = client.updateAccountService(id_account, int(id_update), '/services', updated_service)

            if updated:
                print('\033[92m', end="")
                print("\nService successfully updated!")
                print('\033[0m', end="")
                time.sleep(0.7)
                return


            input("(1) Return ")
            return

    print("\nService not found!\n")
    input("(1) Return ")
    return


def remove_service(account_id):

    clear()
    print("Select the service to ",end="")
    colorprint("remove",'red')
    print("\n---------------------------------------------------------\n")

    current_services = client.getServices(f'/services/?id_account={account_id}')

    for service in current_services:
        print("")
        name_service = service['name']
        colorprint('Service: ', "green")
        print(name_service)
        
        email = service['userEmailService']
        print("Email: "+email)

        password = service['servicePassword']
        print("Password: "+password)
        
        url = service['site']
        print("Website Url: "+url)

        id = service['id_service']
        print("Service ",end ='')
        colorprint("ID", 'green')
        print(": "+ str(id))

    id_remove = input("\nInsert the ID to remove: ")
    
    for current_service in current_services: 
        if current_service['id_service'] == int(id_remove):
            removed = client.deleteAccountService(account_id, int(id_remove), '/services')

            if removed :
                print('\033[92m',end="")
                print("\nService successfully removed!")
                print('\033[0m',end="")
                time.sleep(0.7)
                return

    print('\033[91m',end="")
    print("\nSome error has occurred!!")
    print('\033[0m',end="")
    time.sleep(0.7)
    return

def print_menu():
   
    for index, menu_option in enumerate(menu_options, start=1):
        print(f"({index}) {menu_option}")
def menu():
    try:
        choice = int(input("\nOption: "))
        return choice
    except ValueError:
        colorprint("Invalid input. Please enter a number.",'red')
        return None
def home(current_account):
    while True:
        clear()
        colorprint('Home', 'green')
        colorprint("                               Logged as: ", 'green')
        print(current_account['user']['name'])  
        print("---------------------------------------------------------\n")
        print_menu()
        current_account_id = current_account['id_account']
        option = menu()

        if option == 1:

            view_all_services(current_account_id)
        elif option == 2:
            add_new_service(current_account_id)
        elif option == 3:
            remove_service(current_account_id)
        elif option == 4:
            update_service(current_account_id)
        else:
            input()  
def login():
    clear()
    colorprint('Login', 'green')
    print("\n---------------------------------------------------------\n")
    email_input = input("Enter email: ")
    password_input = pwinput.pwinput(prompt="Enter password: ")
    paylaod = { "email": email_input, "password": password_input}
    account = client.signIn(paylaod, '/login')

    if(account):
        return home(account)
    else: 
        login()
        
# fazer o codigo main aqui 
if __name__ == '__main__':
    login()