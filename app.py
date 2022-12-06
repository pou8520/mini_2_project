from flask import Flask, render_template, request, jsonify
import pymysql
app = Flask(__name__)

# database에 접근
db = pymysql.connect( host='host=secendproj.cczokkdg0lti.ap-northeast-1.rds.amazonaws.com',
                      port=3306,
                      user='admin',
                      passwd='roqkfwkehlrhtlqwh',
                      db='2_project',
                      charset='utf8')

# database를 사용하기 위한 cursor를 세팅합니다.
cursor = db.cursor()

@app.route("/")
def index():
  sql = '''SELECT id FROM test_table'''
  cursor.execute(sql)
  data_id = cursor.fetchall()
  return render_template('index.html', data_id = data_id)

# GET 구현
@app.route("/reload_profile", methods=["GET"])
def profile_get():
  sql = '''SELECT * FROM users'''
  cursor.execute(sql)
  data_list = cursor.fetchall()
  return jsonify({'data_list': data_list})

# POST 구현
@app.route("/save_comment", methods=["POST"])
def comment_post():
  name_receive = request.form['name_give']
  comment_receive = request.form['comment_give']
  print(name_receive)
  sql =f'''INSERT INTO test_table(name, comment)
        VALUES('{name_receive}', '{comment_receive}');'''
  cursor.execute(sql)
  db.commit()
  return jsonify({'msg':'게시글 입력 완료!'})

# DELETE 구현
@app.route("/delete", methods=["DELETE"])
def comment_delete():
  id_receive = request.form['id']
  sql = f'''DELETE FROM test_table
            WHERE id = {id_receive};'''
  cursor.execute(sql)
  db.commit()
  return jsonify({'msg':'게시글 삭제!'})


if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)
