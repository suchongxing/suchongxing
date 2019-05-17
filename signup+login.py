from flask import Flask,request,jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import aaa.signup_login
class User(object):
    def __init__(self,username, password):
        self.username = username
        self.password = password
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)
users = {}
app.register_blueprint(aaa.signup_login.suchongxing)#导入实例，知道实例在这哪里，路径 register_blueprint固定格式
app.register_blueprint(aaa.zxc.vvv)
@app.route('/signup', methods=['POST'])
def signup():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400
    if username in users:
        return jsonify({"msg": "This username have used!"}),201
    users[username]=User(username,password)
    return jsonify({"msg": "Signup success!"}), 200

@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if (not username) or (not password):
        return jsonify({"msg": "Missing username or password parameter"}), 400
    loginuser = aaa.qwe.users.get(username,None)
    if loginuser and loginuser.password==password:
        return jsonify(access_token=create_access_token(identity=username)), 200
    else:
        return jsonify({"msg":"Username or password is not correct!"}), 401

# @app.route('/protected', methods=['GET'])
# @jwt_required
# def protected():
#     # Access the identity of the current user with get_jwt_identity
#     current_user = get_jwt_identity()
#     return jsonify(logged_in_as=current_user), 200
@app.route('/tall', methods=['POST'])
@jwt_required
def tall():
    # if not request.is_json:
    #     return jsonify({"msg": "params is not json"}), 400
    # SanForm =request.json.get("沙雕")
    return jsonify({"answer":"你是不是傻"}), 400

if __name__ == "__main__":
    app.run(port=5001)
