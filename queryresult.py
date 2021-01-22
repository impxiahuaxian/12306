import sys
import os
import requests
from ui import ui_queryresult
from getstation import GetStationInfo
from db_queryresult import QueryResultDB
from buytickets import BuyTickets
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem, QHeaderView, QAbstractItemView

class QueryResult(ui_queryresult.Ui_Form,QWidget):

    def __init__(self):
        super(QueryResult, self).__init__()
        self.ui = ui_queryresult.Ui_Form()
        self.ui.setupUi(self)
        self.train_count = 0

        self.city_code = GetStationInfo()
        self.db_query = QueryResultDB()
        self.buy_ticket = BuyTickets()

        self.ui.tableWidget.setColumnCount(17)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setWindowTitle("查询结果")
        self.resize(1080, 480)

        self.tabalHeader = []
        self.tabalHeader.extend(["车次", "出发站", "到达站"])
        self.tabalHeader.extend(["出发时间", "到达时间", "历时"])
        self.tabalHeader.extend(["商务座", "一等座", "二等座"])
        self.tabalHeader.extend(["高级软卧", "软卧", "动卧", "硬卧"])
        self.tabalHeader.extend(["软座", "硬座", "无座", "备注"])

        self.ui.tableWidget.setHorizontalHeaderLabels(self.tabalHeader)
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.ui.tableWidget.cellDoubleClicked.connect(self.select_seat)

    def train_number(self, url, cookies):
        header = {
            "User - Agent": "Mozilla / 5.0(X11;Ubuntu;Linux x86_64;rv: 71.0) Gecko / 20100101Firefox / 71.0"
            }
        r = requests.get(url, headers=header, cookies=cookies)
        r.encoding = r.apparent_encoding

        data_dict = r.json()
        data_list = data_dict.get('data').get('result')

        path = os.getcwd() + '/data'
        if not os.path.exists(path):
            os.mkdir(path)
        file = open(path + '/train_info.txt', 'w')
        id_query_result = 0
        for string in data_list:
            items = string.split('|')
            id_query_result = id_query_result + 1
            self.db_query.set_query_result(id_query_result, items)
            from_name, to_name = self.city_code.get_station_name(items[6], items[7])
            file.write(items[3] + '|' + from_name + '|' + to_name + '|')
            file.write(items[8] + '|' + items[9] + '|' + items[10] + '|')
            file.write(items[32] + '|' + items[31] + '|' + items[30] + '|')
            file.write(items[21] + '|' + items[23] + '|' + items[33] + '|')
            file.write(items[28] + '|' + items[24] + '|' + items[29] + '|')
            file.write(items[26] + '|' + items[11])
            file.write('\n')
        file.close()
        return len(data_list)

    def table_train_info(self):
        self.textline = []
        file = "./data/train_info.txt"
        with open(file, 'r') as fd:
            for i in range(self.traincount):
                line = fd.readline()
                self.textline.append(line)
        fd.close()
        for i in range(self.traincount):
            tmpList = self.textline[i].split('|')
            for j in range(len(tmpList)):
                if tmpList[j] == '':
                    tmpList[j] = '-'
                item = QTableWidgetItem(tmpList[j])
                self.ui.tableWidget.setItem(i, j, item)

    def select_seat(self):
        self.setVisible(False)
        item_selected = self.ui.tableWidget.selectedItems()
        row_selected = item_selected[0].row()+1
        #column_selected = item_selected[0].column()+1
        tuple_train_num = self.db_query.get_query_train_num(row_selected)
        train_num = list(tuple_train_num)[0]
        #seat_num = column_selected-5
        print("双击")
        print(train_num)
        self.buy_ticket.set_driver(self.driver)
        self.buy_ticket.set_passengers(self.passengers)
        self.buy_ticket.is_ticket(train_num)
        self.buy_ticket.send_message(self.phone_num)

        self.driver.quit()

    def set_table_row(self, row):
        self.traincount = row
        self.ui.tableWidget.setRowCount(row)

    def set_driver(self, driver):
        self.driver = driver

    def set_passengers(self, passengers):
        self.passengers = passengers

    def set_phone_num(self, phoneNum):
        self.phone_num = phoneNum


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QueryResult()
    win.set_table_row(28)
    win.table_train_info()
    win.show()
    sys.exit(app.exec_())