from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import QtGui
from query import Query
from ui import ui_login
import base64
import time
import json
import sys

class Login(ui_login.Ui_Form, QWidget):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = ui_login.Ui_Form()
        self.ui.setupUi(self)
        self.coordinate = [[-105, -20], [-35, -20], [40, -20], [110, -20],
                           [-105, 50], [-35, 50], [40, 50], [110, 50]]

        self.ui.okBtn.clicked.connect(self.on_ok_clicked)

    def get_verify_image(self, driver):
        try:
            img_element = WebDriverWait(driver, 100).until(
                EC.presence_of_element_located((By.ID, "J-loginImg"))
            )
        except Exception as e:
            print("网络开小差，请稍后尝试")

        base64_str = img_element.get_attribute("src").split(",")[-1]
        imgdata = base64.b64decode(base64_str)
        with open('./images/verify.jpg', 'wb') as file:
            file.write(imgdata)
        self.img_element = img_element
        time.sleep(5)
        img_verify = QtGui.QPixmap("./images/verify.jpg").scaled(
            self.ui.verifyLabel.width(), self.ui.verifyLabel.height())
        self.ui.verifyLabel.setPixmap(img_verify)
        return True

    def on_ok_clicked(self):
        self.setVisible(False)
        result = []
        position = self.ui.lineEdit.text()
        list_position = position.split(',')
        for i in range(len(list_position)):
            result.append(int(list_position[i]))
        print(result)
        self.result = result
        self.move_and_click(self.driver)
        time.sleep(1)
        self.submit(self.driver)
        self.query = Query()
        self.query.set_driver(self.driver)
        self.query.show()

    def move_and_click(self, driver):
        try:
            Action = ActionChains(driver)
            for i in self.result:
                Action.move_to_element(self.img_element).\
                    move_by_offset(self.coordinate[i][0], self.coordinate[i][1]).click()
            Action.perform()
        except Exception as e:
            print(e.message())

    def submit(self, driver):
        driver.find_element_by_id("J-login").click()
        time.sleep(5)

    def save_cookie(self):
        cookies = self.driver.get_cookies()
        tmp_dict = {}
        with open("./data/cookies", 'w') as f:
            f.write('')
        for cookie in cookies:
            tmp_dict[cookie['name']] = cookie['value']
            cookieStr = json.dumps(tmp_dict)
            with open("./data/cookies", 'a+') as f:
                f.write(cookieStr)
                f.write('\n')

    def set_driver(self, driver):
        self.driver = driver


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec_())
