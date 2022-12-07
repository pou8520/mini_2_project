from flask import Flask, render_template, request, jsonify
import pymysql 
app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')

# GET 구현
@app.route("/comment/<int:page_id>", methods=["GET"])
def comment_get(page_id):
  db = pymysql.connect( host='secendproj.cczokkdg0lti.ap-northeast-1.rds.amazonaws.com',
                        port=3306,
                        user='admin',
                        passwd='roqkfwkehlrhtlqwh',
                        db='2_project',
                        charset='utf8')
  cursor = db.cursor()

  if page_id == 1:
    sql =  '''SELECT * FROM pagination
              LIMIT 10 OFFSET 0;'''
  if page_id == 2:
    sql =  '''SELECT * FROM pagination
              LIMIT 10 OFFSET 10;'''
  if page_id == 3:
    sql =  '''SELECT * FROM pagination
              LIMIT 10 OFFSET 20;'''
  if page_id == 4:
    sql =  '''SELECT * FROM pagination
              LIMIT 10 OFFSET 30;'''
  if page_id == 5:
    sql =  '''SELECT * FROM pagination
              LIMIT 10 OFFSET 40;'''

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
  sql = f'''INSERT INTO pagination(name, comment)
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
  sql = f'''DELETE FROM pagination
            WHERE id = {id_receive};'''
  cursor.execute(sql)

  db.commit()
  db.close()
  return jsonify({'msg':'게시글 삭제!'})

# PUT 구현
@app.route("/put", methods=["PUT"])
def comment_put():
  db = pymysql.connect( host='secendproj.cczokkdg0lti.ap-northeast-1.rds.amazonaws.com',
                        port=3306,
                        user='admin',
                        passwd='roqkfwkehlrhtlqwh',
                        db='2_project',
                        charset='utf8')
  cursor = db.cursor()

  id_receive = request.form['id']
  correction_receive = request.form['correction_give']
  sql = f'''UPDATE pagination
            SET comment = '{correction_receive}'
            WHERE id = {id_receive};'''
  cursor.execute(sql)

  db.commit()
  db.close()
  return jsonify({'msg':'게시글 수정 완료!'})

if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)