import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import pymysql

## 회원 가입 프로그램


form_class = uic.loadUiType("ui/join2.ui")[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("회원가입프로그램")

        self.idcheck_btn.clicked.connect(self.idCheck)
        self.reset_btn.clicked.connect(self.reset)
        self.join_btn.clicked.connect(self.memberJoin)
        self.login_btn.clicked.connect(self.memberLogin)


    def idCheck(self):
        memberid = self.memberid_edit.text()  # 회원 아이디로 입력된 아이디 텍스트 가져오기

        conn = pymysql.connect(host="localhost", user="root", password="12345",
                               db="memberdb")  # 1.db와 파이썬 파일 사이의 연결통로가 생성

        sql = f"SELECT * FROM member WHERE memberid='{memberid}'"

        cur = conn.cursor()
        cur.execute(sql)

        result = cur.fetchone()

        if result == None: # 회원가입가능
            QMessageBox.warning(self,'가입가능',"입력하신 아이디는 가입 가능한 아이디입니다. 계속해서 가입 진행하세요.")

        else:
            QMessageBox.warning(self, '가입불가',"입력하신 아이디는 이미 존재하는 아이디입니다. 다른 아이디를 입력하세요.")

        cur.close()
        conn.close()

    def memberJoin(self):

        memberid = self.memberid_edit.text()  # 회원아이디로 입력된 아이디 텍스트 가져오기
        memberpw = self.memberpw_edit.text()  # 회원비밀번호 텍스트 가져오기
        name = self.name_edit.text()  # 회원비밀번호 텍스트 가져오기
        phone = self.phone_edit.text()  # 회원전화번호 텍스트 가져오기
        address = self.address_edit.text()  # 회원주소 텍스트 가져오기
        age = self.age_edit.text()  # 회원나이 텍스트 가져오기
        print(memberid)
        print(memberpw)
        print(name)
        print(phone)
        print(age)

        conn = pymysql.connect(host='localhost', user='root', password='12345', db='memberdb')

        sql = f"INSERT INTO member VALUES ('{memberid}', '{memberpw}', '{name}', '{phone}', '{address}', {age})"

        cur = conn.cursor()  # 커서 생성
        cur.execute(sql)  # SQL문 실행

        cur.close()
        conn.commit()
        conn.close()

    def memberLogin(self):
        print("74")
        loginid = self.loginid_edit.text() # 로그인 아이디로 입력된 아이디 텍스트 가져오기
        loginpw = self.loginpw_edit.text()  # 로그인 비밀번호로 텍스트 가져오기
        print("77")
        conn = pymysql.connect(host="localhost", user="root", password="12345", db="memberdb")  # 1.db와 파이썬 파일 사이의 연결통로가 생성
        print("80")
        sql = f"SELECT * FROM member WHERE memberid='{loginid}' and memberpw='{loginpw}'"
        print("82")
        cur = conn.cursor()
        cur.execute(sql)

        result = cur.fetchone()
        print(result)

        if result == None:
            self.logintext_label.setText("로그인 실패. 다시 확인하세요!")

        else:
            self.logintext_label.setText("로그인 성공")


            cur.close()
            conn.close()


    def reset(self):
        self.memberid_edit.clear()
        self.memberpw_edit.clear()
        self.name_edit.clear()
        self.phone_edit.clear()
        self.address_edit.clear()
        self.age_edit.clear()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

