import requests
import sqlite3

class GetStationInfo():
    def __init__(self):
        self.url = 'https://www.12306.cn/index/script/core/common/station_name_v10072.js'
        self.headers = {"User - Agent":
                       "Mozilla / 5.0(X11;Ubuntu;Linux x86_64;rv: 71.0) Gecko / 20100101Firefox / 71.0"
        }

    def initdatabase(self):
        self.db = sqlite3.connect('./database/citycode.db')

    def get_station_name_code(self):
        self.initdatabase()
        cursor = self.db.cursor()

        resp = requests.get(self.url, headers=self.headers)
        resp.encoding = resp.apparent_encoding
        # data_dict = resp.json()
        data_str = resp.text.strip("var station_names =';")
        data_list = data_str.split('@')[1:]
        data_dict = {}
        item_count = 0
        for item in data_list:
            item_count = item_count + 1
            temp_list = item.split('|')
            data_dict[temp_list[1]] = temp_list[2]
            sql_name_and_code = "insert or ignore into citycode(city,code) values('{}','{}');"\
                .format(temp_list[1], temp_list[2])
            cursor.execute(sql_name_and_code)
        cursor.close()
        self.db.commit()
        self.db.close()

    def get_station_code(self, from_station, to_station):
        self.initdatabase()
        cursor = self.db.cursor()
        sql_get_from_station_code = "select code from citycode where city='{}';"\
            .format(from_station)
        sql_get_to_station_code = "select code from citycode where city='{}';" \
            .format(to_station)
        tuple_from_station_code = cursor.execute(sql_get_from_station_code).fetchone()
        tuple_to_station_code = cursor.execute(sql_get_to_station_code).fetchone()
        from_station_code = list(tuple_from_station_code)[0]
        to_station_code = list(tuple_to_station_code)[0]
        return from_station_code, to_station_code

    def get_station_name(self, from_station, to_station):
        self.initdatabase()
        cursor = self.db.cursor()
        sql_get_from_station_code = "select city from citycode where code='{}';"\
            .format(from_station)
        sql_get_to_station_code = "select city from citycode where code='{}';" \
            .format(to_station)
        tuple_from_station_name = cursor.execute(sql_get_from_station_code).fetchone()
        tuple_to_station_name = cursor.execute(sql_get_to_station_code).fetchone()
        from_station_name = list(tuple_from_station_name)[0]
        to_station_name = list(tuple_to_station_name)[0]
        return from_station_name, to_station_name

if __name__ == '__main__':
    getstation = GetStationInfo()
    getstation.get_station_name_code()