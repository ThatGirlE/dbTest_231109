# 1 DB가 설치된 컴퓨터의 IP주소(내 컴퓨터에 DB가 설치되어 있으면 localhost)
# 2 DB의 계정 root
# 3 db의 비밀번호 12345
# 4 db(스키마)의 이름(ex:memberdb)

import pymysql

conn = pymysql.connect(host="localhost", user="root", password="12345", db="memberdb")# 1.db와 파이썬 파일 사이의 연결통로가 생성

sql = 'SELECT * FROM member' # 2.sql문 생성하여 문자열로 저장

cur = conn.cursor() # 3. 커서 생성
cur.execute(sql) # 4. sql문 실행

result = cur.fetchall() # 튜플 안에 튜플로 반환

print(result)

for member in result:
    print(member[2]) # 회원들의 이름만 출력


cur.close()
conn.close()
