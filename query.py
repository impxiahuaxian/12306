from ui import ui_query
from queryresult import QueryResult
from getstation import GetStationInfo
import sys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from PyQt5.QtWidgets import QWidget, QApplication, QCalendarWidget
class Query(ui_query.Ui_Form,QWidget):
    def __init__(self):
        super(Query, self).__init__()
        self.ui = ui_query.Ui_Form()
        self.ui.setupUi(self)

        self.from_station = "北京"
        self.to_station = "上海"
        self.train_date = "2020-05-20"

        self.calendar = QCalendarWidget()
        self.query_result = QueryResult()
        self.city_code = GetStationInfo()
        self.show_date()

        self.ui.dataTBtn.clicked.connect(self.select_date)
        self.ui.qureyBtn.clicked.connect(self.on_query_clicked)

    def query(self, driver):
        query_url = "https://www.12306.cn/index/"
        driver.get(query_url)
        time.sleep(2)

        input_from_station = driver.find_element_by_id("fromStationText")
        input_from_station.send_keys(Keys.CONTROL + "a")
        input_from_station.send_keys(Keys.BACKSPACE)
        input_from_station.send_keys(self.from_station)
        input_from_station.send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element_value((By.ID, "fromStationText"), self.from_station))

        input_to_station = driver.find_element_by_id("toStationText")
        input_to_station.send_keys(self.to_station)
        input_to_station.send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element_value((By.ID, "toStationText"), self.to_station))

        input_train_date = driver.find_element_by_id("train_date")
        driver.execute_script('arguments[0].value="{}"'.format(self.train_date), input_train_date)
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element_value((By.ID, "train_date"), self.train_date))

        queryButton = driver.find_element_by_id('search_one')
        queryButton.click()

        n = driver.window_handles
        driver.switch_to.window(n[-1])
        self.query_result.set_driver(driver)

    def select_date(self):
        self.calendar.show()
        self.calendar.selectionChanged.connect(self.show_date)
        self.calendar.activated.connect(self.calendar.close)

    def show_date(self):
        selectDate = self.calendar.selectedDate()
        showDate = selectDate.toString("yyyy-MM-dd")
        self.ui.dataTBtn.setText(showDate)
        return

    def get_cookies(self):
        cookies = self.driver.get_cookies()
        dict_cookies = {}
        for cookie in cookies:
            dict_cookies[cookie['name']] = cookie['value']
        if dict_cookies.get('RAIL_DEVICEID') and dict_cookies.get('RAIL_EXPIRATION'):
            print("ok")
        return dict_cookies

    def on_query_clicked(self):
        self.from_station = self.ui.startCityLine.text()
        self.to_station = self.ui.endCityLine.text()
        self.train_date = self.ui.dataTBtn.text()
        passengers = self.ui.passengersLine.text()
        phone_num = self.ui.phoneNumLine.text()
        self.setVisible(False)
        self.query(self.driver)
        from_station_code, to_station_code = self.city_code.get_station_code(
            self.from_station, self.to_station)
        cookies = self.get_cookies()
        query_result_url = "https://kyfw.12306.cn/otn/leftTicket/query?" \
                           "leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&" \
                           "leftTicketDTO.to_station={}&purpose_codes=ADULT"\
            .format(self.train_date, from_station_code, to_station_code)

        print(query_result_url)

        train_count = self.query_result.train_number(query_result_url, cookies)
        self.query_result.set_table_row(train_count)
        self.query_result.set_passengers(passengers)
        self.query_result.set_phone_num(phone_num)
        self.query_result.table_train_info()
        self.query_result.show()

    def set_driver(self, driver):
        self.driver = driver



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Query()
    win.show()
    sys.exit(app.exec_())