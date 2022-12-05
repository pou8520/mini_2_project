from flask import Flask, render_template, request, jsonify
import pymysql 
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

# database에 접근
db = pymysql.connect( host='localhost',
                      port=3306,
                      user='root',
                      passwd='changmin94!',
                      db='project',
                      charset='utf8')

# database를 사용하기 위한 cursor를 세팅합니다.
cursor = db.cursor()

# SQL query 작성
# sql =  '''CREATE TABLE test_table(
#           id  INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
#           name VARCHAR(100) NOT NULL,
#           comment VARCHAR(100) NOT NULL,
#           note VARCHAR(100) NOT NULL
#           );'''

# SQL query 작성, insert
sql ='''INSERT INTO test_table(name, comment, note)
        VALUES('정창민', '창민이는 나혀니를 좋아한다.', '비고임');'''

# SQL query 실행
cursor.execute(sql)

# SQL query가 잘 실행됐는지 table을 살펴보도록 합니다.
# 이미 4번 라인에서 use database를 수행한 것과 다름 없으니 show tables라는 명령을 수행해도 문제가 없습니다.
cursor.execute("show tables") 

# 데이터 변화 적용
# CREATE 혹은 DROP, DELETE, UPDATE, INSERT와 같이 Database 내부의 데이터에 영향을 주는 함수의 경우 commit()을 해주어야 합니다.
db.commit()

# Database 닫기
db.close()

if __name__ == '__main__':
  app.run('0.0.0.0', port=3306, debug=True)