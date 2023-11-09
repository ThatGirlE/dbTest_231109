import pymysql

conn = pymysql.connect(host='localhost', user='root', password='12345', db='testdb')

# 0. 회원조회 -> 정보를 조회할 아이디를 입력하세요:->아이디를 입력한 회원의 정보가 출력
print("1. 회원 가입")
print("2. 회원비밀번호수정")
print("3. 회원정보삭제")
print("4. 회원리스트 조회")

menu = input("위 메뉴 중 한 가지를 선택하세요 : ")

if menu == '1':
    print("----- 회원가입 -----")
    memberId = input("1. 회원아이디 : ")
    memberPw = input("2. 회원비밀번호 : ")
    memberName = input("3. 회원이름 : ")
    memberPhone = input("4. 회원전화번호 : ")
    sql = f"INSERT INTO member2 VALUES ('{memberId}', '{memberPw}', '{memberName}', '{memberPhone}')"
    cur = conn.cursor()
    cur.execute(sql)  # sql문 실행
elif menu == '2':
    updateId = input("비밀번호를 수정할 회원의 아이디를 입력하세요 : ")
    memberPw = input("수정할 회원비밀번호 : ")
    sql = f"UPDATE INTO member2 SET memberpw='{memberPw}' WHERE memberid='{updateId}'"
    cur = conn.cursor()
    cur.execute(sql)  # sql문 실행
elif menu == '3':
    removeId = input("삭제할 회원의 아이디를 입력하세요 : ")
    sql = f"DELETE FROM member2 WHERE memberid='{removeId}'"
    cur = conn.cursor()
    cur.execute(sql)  # sql문 실행
else:
    pass


sql2 = 'SELECT * FROM member2'

cur = conn.cursor()
cur.execute(sql2) # SQL문 실행

rows = cur.fetchall() # 해당 테이블의 모든 레코드가 튜플구조로 반환됨

# print(rows)

print("=========== 회원 전체 리스트 조회 =============")
print("회원아이디 / 비밀번호 / 회원이름 / 전화번호")
for member in rows:
    print(member)

cur.close()
conn.commit() # insert, delete, update 사용했을 경우에는 commit을 반드시 해줘야 함!
conn.close()