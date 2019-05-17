from flask import Flask, jsonify, request

class User(object):
    def __init__(self,yonghuming,mima):
        self.yonghuming =yonghuming
        self.mima = mima

duixiang = Flask(__name__)
user = {}
@duixiang.route('/zhuce', methods=['POST'])
def zhuce():
    if not request.is_json:
        return jsonify({"msg":"Missing Json in request"}),400
    # yonghuming = request.form['yonghuming']
    # mima = request.form['mima']

    # yonghuming = request.agrs.get('yonghuming', None)
    # mima = request.agrs.get('mima', None)
    #
    yonghuming = request.json.get('yonghuming',None)
    mima = request.json.get('mima', None)
    if not yonghuming:
      return jsonify({"msg": "不是用户名"}), 400
    if not mima:
        return jsonify({"msg": "密码错误"}), 400
    if yonghuming in user:
        return jsonify({"msg": "该用户已注册，请使用账户密码登录"}),201
    user[yonghuming] = User(yonghuming,mima)
    return jsonify({"msg": "注册成功"}),200
if __name__ == '__main__':
    duixiang.run()
