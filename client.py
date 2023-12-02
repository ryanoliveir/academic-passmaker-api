from model.client import Client


# classe para pegar e mandar dados para a api
client = Client('http://localhost:5000', '/api' )



#clarar outras funções aqui



# fazer o codigo main aqui 

if __name__ == '__main__':
    print('Welcome to PASSMaker !')



    services = client.getServices('/services')

    client.printJson(services)