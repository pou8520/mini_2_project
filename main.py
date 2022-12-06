from flask import Flask, render_template, request
import pymysql
import json
# import hashlib

app = Flask(__name__)

# db = pymysql.connect(host='127.0.0.1',
#                      port=3306,
#                      user='root',
#                      passwd='qwe[]!23',
#                      db='2_project',
#                      charset='utf8')

db = pymysql.connect(host='secendproj.cczokkdg0lti.ap-northeast-1.rds.amazonaws.com', port=3306, user='admin',
                     passwd='roqkfwkehlrhtlqwh', db='2_project', charset='utf8')


cursor = db.cursor()


@app.route('/')
def login_signup_page():
    return render_template('first_page.html')

@app.route('/index.html')
def login_success():
    return render_template('index.html')


@app.route("/signup", methods=["POST"])
def signup_btn_click():

    name_receive = request.form['name_give']
    email_receive = request.form['email_give']
    password_receive = request.form['password_give']

    sql = f'''INSERT INTO signup(name, email, pw)
        VALUES('{name_receive}', '{email_receive}','{password_receive}');'''
    cursor.execute(sql)
    db.commit()
    return jsonify({'msg': '회원가입 완료!'})

# 로그인 기능 구현


# @app.route('/login', methods=['POST'])
# def login_btn_click():

#     username = request.form['name_give']
#     password = request.form['password_give']

#     sql = f'''SELECT * FROM signup WHERE username = %s AND password = %s; '''
#     account = cursor.fetchone()

#     if account:
#         session['loggedin'] = True
#         session['id'] = account['id']
#         session['username'] = account['username']
#         return '로그인 성공!'
#     else:
#         msg = '로그인 실패!'


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
