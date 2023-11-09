import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import pymysql


form_class = uic.loadUiType("ui/member.ui")[0]  # 1

class MainWindow(QMainWindow, form_class): #2
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("회원조회프로그램")

        self.search_btn.clicked.connect(self.db_search) # 조회버튼 클릭시 db_search 함수 호출
        self.modify_btn.clicked.connect(self.db_modify) # 회원정보수정 클릭시 db_modify 함수 호출
        self.reset_btn.clicked.connect(self.reset)


    def db_search(self):  #3
        memberid = self.memberid_edit.text() # 회원 아이디로 입력된 아이디 텍스트 가져오기

        conn = pymysql.connect(host="localhost", user="root", password="12345",
                               db="memberdb")  # 1.db와 파이썬 파일 사이의 연결통로가 생성

        sql = f"SELECT * FROM member WHERE memberid='{memberid}'"

        cur = conn.cursor()
        cur.execute(sql)

        result = cur.fetchone()

        cur.close()
        conn.close()

        #print(result)

        if result != None:

            self.memberpw_edit.setText(result[1])
            self.name_edit.setText(result[2])
            self.phone_edit.setText(result[3])
            self.address_edit.setText(result[4])
            self.age_edit.setText(str(result[5]))  # age 정수여서 문자열로 변환
        else:

            self.memberpw_edit.setText("회원정보없음")
            self.name_edit.setText("회원정보없음")
            self.phone_edit.setText("회원정보없음")
            self.address_edit.setText("회원정보없음")
            self.age_edit.setText("회원정보없음")


    def db_modify(self):

        memberid = self.memberid_edit.text()  # 회원 아이디로 입력된 아이디 텍스트 가져오기
        memberpw = self.memberpw_edit.text()  # 회원 비밀번호 텍스트 가져오기
        name = self.name_edit.text()   # 회원 이름 텍스트 가져오기
        phone = self.phone_edit.text()  # 회원 번호 텍스트 가져오기
        address = self.address_edit.text()   # 회원 주소 텍스트 가져오기
        age = self.age_edit.text()  # 회원 나이 텍스트 가져오기


        conn = pymysql.connect(host="localhost", user="root", password="12345",
                               db="memberdb")
        sql = f"UPDATE member SET memberpw='{memberpw}',name='{name}',phone='{phone}',address='{address}',memberage='{age}' WHERE memberid = '{memberid}'"

        cur = conn.cursor()
        cur.execute(sql)


        cur.close()
        conn.commit()
        conn.close()

        self.db_search()   # 다시 데이터 갱신



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
