from flask import Flask, render_template, request, session
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

app.secret_key = 'your secret key'

@app.route('/')
def login_page():
    return render_template('login.html')


@app.route('/signup')
def signup_page():
    return render_template('signup.html')


@app.route('/main')
def main_page():
    return render_template('index.html')

# 로그인 기능


@app.route('/', methods=['GET', 'POST'])
def login_btn():
    db = pymysql.connect(host='secendproj.cczokkdg0lti.ap-northeast-1.rds.amazonaws.com', port=3306, user='admin',
                         passwd='roqkfwkehlrhtlqwh', db='2_project', charset='utf8')
    cursor = db.cursor()

    msg = ''

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:

        username = request.form['username']
        password = request.form['password']

        cursor.execute(
            'SELECT * FROM accounts WHERE username = %s AND pw = %s', (username, password))

        account = cursor.fetchone()
        print(account)

        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]
            msg = '로그인 성공'
            return render_template('index.html', msg=msg)
        else:
            msg = '로그인 실패!'
    return render_template('login.html', msg=msg)

# 회원가입 기능


@app.route("/signup", methods=["POST"])
def signup_btn_click():

    db = pymysql.connect(host='secendproj.cczokkdg0lti.ap-northeast-1.rds.amazonaws.com', port=3306, user='admin',
                         passwd='roqkfwkehlrhtlqwh', db='2_project', charset='utf8')
    cursor = db.cursor()

    name_receive = request.form['name_give']
    nickname_receive = request.form['nickname_give']
    email_receive = request.form['email_give']
    password_receive = request.form['password_give']

    sql = f'''INSERT INTO accounts(username, nickname, email, pw)
        VALUES('{name_receive}','{nickname_receive}','{email_receive}','{password_receive}');'''
    cursor.execute(sql)
    db.commit()
    return jsonify({'msg': '회원가입 완료!'})




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
