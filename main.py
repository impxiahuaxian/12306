from login import Login
from PyQt5.QtWidgets import QWidget, QApplication
from selenium import webdriver
import sys
import time
from ui import ui_main

class MainProgram(ui_main.Ui_Form, QWidget):

    def __init__(self):
        super(MainProgram, self).__init__()
        self.ui = ui_main.Ui_Form()
        self.ui.setupUi(self)

        self.userName = ''
        self.passWord = ''
        self.loginVar = Login()

        self.ui.LoginBtn.clicked.connect(self.on_login_clicked)

    #
    # 该方法驱动浏览器访问12306登录页面，选择账号登录，并输入用户名和密码
    def login(self):
        login_url = "https://kyfw.12306.cn/otn/resources/login.html"
        self.driver = webdriver.Chrome("./driver/chromedriver.exe")
        self.driver.set_window_size(1200, 900)
        self.driver.get(login_url)
        account = self.driver.find_element_by_class_name("login-hd-account")
        account.click()

        userName = self.driver.find_element_by_id("J-userName")
        userName.send_keys(self.userName)
        passWord = self.driver.find_element_by_id("J-password")
        passWord.send_keys(self.passWord)

    #
    # 该方法获取用户输入的用户名和密码，调用login方法输入用户名和密码
    # 并且调用验证码模块，获取验证码图片
    def on_login_clicked(self):
        self.setVisible(False)
        self.userName = self.ui.userName.text()
        self.passWord = self.ui.passWd.text()
        self.login()
        time.sleep(1)
        self.loginVar.set_driver(self.driver)
        flag = self.loginVar.get_verify_image(self.driver)
        if flag:
            self.loginVar.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainUI = MainProgram()
    mainUI.show()
    sys.exit(app.exec_())