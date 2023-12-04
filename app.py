from flask import Flask, request, jsonify, make_response, Blueprint
from database.db import Database
from model.service import Service
from model.password import Password

app = Flask(__name__)

db = Database()
db.init()

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/users')
def users():
    
    users_list = db.get_users()
    response = []
    for user in users_list:

        currentUser = {
            'id_user': user.id_user, 
            'name': user.email ,
            'email': user.email
        }

        response.append(currentUser)
        
    return make_response(jsonify(response), 200)


@api.route('/services/', methods=['GET', 'POST', 'DELETE'])
def services():

    if request.method == 'GET':
        response = []
        args = request.args

        if args:
            
            account_services_list  = db.get_AccountServices(int(args.get('id_account')))
            for service in account_services_list:

                currentServices = {
                    'id_service': service.id_service, 
                    'name': service.name,
                    'site': service.site, 
                    'userEmailService': service.userEmailService, 
                    'servicePassword': service.servicePassword
                }

                response.append(currentServices)
            
            return make_response(jsonify(response), 200)
        else:
             return make_response(jsonify({"error": "args missing"}), 400)

    elif request.method == 'POST':
        body = request.get_json()

        account_id = int(body['account_id'])
        newPassword = Password(body['servicePassword'])

        newService = Service(
            body['name'], 
            body['site'], 
            body['userEmailService'],
            newPassword
        )


        db.createService(newService, account_id)
        
        return make_response(jsonify({'message': 'Sucesss', 'status': 200}))

    elif request.method == 'DELETE':

        serviceDeleted = False
        args = request.args

        account_id = int(args.get('id_account'))
        service_id = int(args.get('id_service'))

        account_services = db.get_AccountServices(account_id)

        for account_service in account_services:
            print('Account service: ' + account_service.name)
            if(account_service.id_service ==  service_id):
                print(f'Account service: {account_service.name} [{service_id}] Must be delete')
                db.delete_AccountService(account_service.id_service, account_id)
                serviceDeleted = True
                

        
        if(serviceDeleted):
            return make_response(jsonify({'message': 'Service removed', 'status': 200},), 200)
        
        return make_response(jsonify({'message': 'Error in delete service', 'status': 400}), 400)

    else:
        return make_response(jsonify({'message': 'Method not allowed', 'status': 405}))


# fix this endpoint !!!
@api.route('/service/', methods=['GET', 'POST'])
def service():

    if request.method == 'GET':

        args = request.args
        services_list = db.get_AccountServices(int(args.get('id_account')))

        response = [
            {
                'id_account':  int(args.get('id_account'))
            }
        ]

        for service in services_list:

            currentService = {
                'id_service': service.id_service, 
                'name': service.name,
                'site': service.site, 
                'userEmailService': service.userEmailService, 
                'servicePassword': service.servicePassword
            }

            response.append(currentService)

        return make_response(jsonify(response), 200)

    else:
         return make_response(jsonify({'message': 'Method not allowed', 'status': 405}))
    

@api.route('/accounts')
def accounts():
    
    accounts_list = db.get_accounts()


    response = []
    for account in accounts_list:

        currentAccount = {
            'id_account': account.id_account, 
            'user': {
                'id_user': account.user.id_user, 
                'name': account.user.email ,
                'email': account.user.email
            },
            'password': account.password, 
            'servicesList': [service.to_dict() for service in account.servicesList], 
            'unlimitedService': account.unlimitedService,
            'servicesAmmount': account.maxServicesAllowed if account.unlimitedService == False else "Unlimited"
        }

        response.append(currentAccount)
        
    return make_response(jsonify(response), 200)


@api.route('/login', methods=['POST'])
def login():
    response_error = { "error": "login error"}
    response_sucess = { "sucess": "login sucess"}
    response = []
    body = request.get_json()

    
    accounts = db.get_accounts()

    for account in accounts:
        if (account.user.email == body['email']) and (account.password == body['password']):
            print(account.user.email, account.password)
        
            response = {
                'id_account': account.id_account,
                'user': { 'name': account.user.name , 'email': account.user.email },
            }

            print(response)

            return make_response(jsonify(response), 200)
        

    return make_response(jsonify(response_error), 401)


@api.route('/')
def index():
    response = { "message": "server ok!"}

    return make_response(jsonify(response),200 )

app.register_blueprint(api)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


    