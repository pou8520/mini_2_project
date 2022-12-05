from flask import Flask, render_template, request, jsonify
import pymysql 
app = Flask(__name__)

# database에 접근
db = pymysql.connect( host='localhost',
                      port=3306,
                      user='root',
                      passwd='changmin94!',
                      db='project',
                      charset='utf8')

# database를 사용하기 위한 cursor를 세팅합니다.
cursor = db.cursor()

@app.route("/")
def index():
  sql = '''SELECT * FROM test_table'''
  cursor.execute(sql)
  data_list = cursor.fetchall()
  return render_template('index.html', data_list = data_list)



if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)