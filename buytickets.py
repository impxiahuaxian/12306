from inc.zhenzismsclient import ZhenziSmsClient
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BuyTickets():

    def __init__(self):
        pass

    def refresh_query(self):
        WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable((By.ID, "query_ticket"))
        )
        print("刷新")
        refreshBtn = self.driver.find_element_by_id("query_ticket")
        refreshBtn.click()
        return

    def buy_ticket(self, tr):
        print("准备点击")
        oderBtn = tr.find_element_by_xpath(".//td[13]/a")
        oderBtn.click()
        time.sleep(10)
        is_passenger = False
        WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, ".//ul[@id='normal_passenger_id']/li"))
        )
        passenger_labels = self.driver.find_elements_by_xpath(
            ".//ul[@id='normal_passenger_id']/li/label"
        )
        for passenger_label in passenger_labels:
            name = passenger_label.text
            if name == self.passengers:
                passenger_label.click()
                is_passenger = True

        if is_passenger == True:
            submitBtn = self.driver.find_element_by_id("submitOrder_id")
            submitBtn.click()
            WebDriverWait(self.driver, 1000).until(
                EC.presence_of_element_located((By.CLASS_NAME, "dhtmlx_wins_body_outer"))
            )
            WebDriverWait(self.driver, 1000).until(
                EC.presence_of_element_located((By.ID, "qr_submit_id"))
            )
            qr_submit = self.driver.find_element_by_id("qr_submit_id")
            qr_submit.click()
            time.sleep(10)
        else:
            print("无此乘车人，请先添加")

        return

    def is_ticket(self, param_train_num):
        print("检查是否有票")
        print(self.driver.current_url)
        WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.XPATH, ".//tbody[@id='queryLeftTable']/tr"))
        )
        tr_list = self.driver.find_elements_by_xpath(".//tbody[@id='queryLeftTable']/tr[not(@datatran)]")
        for tr in tr_list:
            train_num = tr.find_element_by_class_name("number").text
            print(train_num)
            if train_num == param_train_num:
                xpath_str = ".//td[4]"
                left_ticket_td = tr.find_element_by_xpath(xpath_str).text
                flag = True
                while flag:
                    if left_ticket_td == '无':
                        print("无票")
                        time.sleep(5)
                        self.refresh_query()
                    elif left_ticket_td == '候补':
                        time.sleep(2)
                        self.refresh_query()
                    else:
                        print("有票")
                        self.buy_ticket(tr)
                        return

    def send_message(self, phone_num):
        client = ZhenziSmsClient('https://sms_developer.zhenzikj.com', '105750', '77e1669d-ddd0-43d3-ae6d-f1afda7e38e9')
        message = "抢到票了，快去APP付款吧，只有三十分钟呦！"
        print(client.send(phone_num, message))
        print("已通知用户！")

    def set_driver(self, driver):
        self.driver = driver

    def set_passengers(self, passengers):
        self.passengers = passengers

if __name__ == '__main__':
    buy = BuyTickets()
    buy.send_message('18253800751')