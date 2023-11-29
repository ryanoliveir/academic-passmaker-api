from flask import Flask, request, jsonify, make_response, Blueprint
from database.db import Database

app = Flask(__name__)

db = Database()
db.init()

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/users')
def users():
    
    users_list = db.get_users()
    response = []
    for user in users_list:
        currentUser = {'id_user': user.id_user, 'name': user.email ,'email': user.email}
        response.append(currentUser)
#
    return make_response(jsonify(response),200 )


@api.route('/')
def index():
    response = { "message": "server ok!"}

    return make_response(jsonify(response),200 )

app.register_blueprint(api)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


    