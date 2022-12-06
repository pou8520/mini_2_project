from flask import Flask, render_template, request, jsonify
import pymysql 
app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')

# GET 구현
@app.route("/comment", methods=["GET"])
def comment_get():
  db = pymysql.connect( host='secendproj.cczokkdg0lti.ap-northeast-1.rds.amazonaws.com',
                      port=3306,
                      user='admin',
                      passwd='roqkfwkehlrhtlqwh',
                      db='2_project',
                      charset='utf8')
  cursor = db.cursor()

  sql = '''SELECT * FROM board'''
  cursor.execute(sql)
  data_list = cursor.fetchall()

  db.close()
  return jsonify({'data_list': data_list})

# POST 구현
@app.route("/save_comment", methods=["POST"])
def comment_post():
  db = pymysql.connect( host='secendproj.cczokkdg0lti.ap-northeast-1.rds.amazonaws.com',
                      port=3306,
                      user='admin',
                      passwd='roqkfwkehlrhtlqwh',
                      db='2_project',
                      charset='utf8')
  cursor = db.cursor()

  name_receive = request.form['name_give']
  comment_receive = request.form['comment_give']
  sql = f'''INSERT INTO board(name, comment)
            VALUES('{name_receive}', '{comment_receive}');'''
  cursor.execute(sql)

  db.commit()
  db.close()
  return jsonify({'msg':'게시글 전송 완료!'})

# DELETE 구현
@app.route("/delete", methods=["DELETE"])
def comment_delete():
  db = pymysql.connect( host='secendproj.cczokkdg0lti.ap-northeast-1.rds.amazonaws.com',
                      port=3306,
                      user='admin',
                      passwd='roqkfwkehlrhtlqwh',
                      db='2_project',
                      charset='utf8')
  cursor = db.cursor()

  id_receive = request.form['id']
  sql = f'''DELETE FROM board
            WHERE id = {id_receive};'''
  cursor.execute(sql)

  db.commit()
  db.close()
  return jsonify({'msg':'게시글 삭제!'})


if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)
