import pymysql

conn = pymysql.connect(host="localhost", user="root", password="12345", db="memberdb")  # 1.db와 파이썬 파일 사이의 연결통로가 생성

#sql = 'INSERT INTO member VALUES('blackcat','12345', '유관순', '010-4444-1123', '경기도 안산시', 61)'
## 2.sql문 생성하여 문자열로 저장 //왜 안돼?

sql = "INSERT INTO member VALUES('blackcat','12345', '유관순', '010-4444-1233', '경기도 안산시', 61)"

cur = conn.cursor()  # 3. 커서 생성
cur.execute(sql)  # 4. sql문 실행

cur.close()
conn.commit() # insert, delete, update sql문을 사용했을 경우에는 반드시 commit 해줘야 함 db에 확정을 내줘야됨
conn.close()