 # Libraries
from flask import Flask,jsonify,Request,request
from flask_restful import reqparse,Api,Resource
import logging
from flask_restful.utils import cors
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()
#logging.basicConfig(filename='HelpDesk_Chatbot.log',level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#print(request)
# Creating Flask app and API
app = Flask(__name__)
api = Api(app)

allow_ip = ['10.0.8.183']

# placing the restapi routing resource

USER_DATA = {
    "admin": "SuperSecretPwd"
}


@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

class test(Resource):
    #@auth.login_required
    @cors.crossdomain(origin=["10.0.7.183"],methods=["GET","POST"],expose_headers="Content-Type,Authorization",credentials=True)
    def post(self):
        '''

        :return:
        '''

        #return "hi"
        print(cors)
        print(dir(cors.make_response))
        return jsonify(foo='cross domain ftw')


allow_ip = ['10.0.8.183']
class test1(Resource):

    def get(self):
        '''

        :return:
        '''

        #return "hi"
        print(request.remote_addr)
        request_ip = request.remote_addr
        if request_ip not in allow_ip:
            return jsonify(status='unauthorized access')
        #print(dir(cors.make_response))
        return jsonify({"foo":'cross domain ftw'})
# @app.route("/get_my_ip", methods=["GET"])
# def get_my_ip():
#     return jsonify({'ip': request.remote_addr}), 200

# User Registration Module
api.add_resource(test,'/test')
# with app.test_client() as client:
#     print(client)
#     res = client.get('/test')
#     print(res.headers)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    # with app.test_client() as client:
    #     res = client.get('/')
    #     print(res)
