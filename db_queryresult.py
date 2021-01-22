import sqlite3

class QueryResultDB():

    def __init__(self):
        pass

    def initdatabase(self):
        self.db = sqlite3.connect('./database/queryresult.db')

    def set_query_result(self, id_result, items):
        self.initdatabase()
        cursor = self.db.cursor()
        for i in range(len(items)):
            if items[i] == ' ':
                items[i] = '-'
        sql_insert_1 = "replace into queryresult values('{}','{}',"\
            .format(id_result, items[3])
        sql_insert_2 ="'{}','{}','{}','{}','{}',"\
            .format(items[32], items[31], items[30], items[21], items[23])
        sql_insert_3 = "'{}','{}','{}','{}','{}');"\
            .format(items[33], items[28], items[24], items[29], items[26])
        sql_insert_query_result = sql_insert_1 + sql_insert_2 + sql_insert_3
        print(sql_insert_query_result)
        cursor.execute(sql_insert_query_result)
        cursor.close()
        self.db.commit()
        self.db.close()

    def get_query_train_num(self, id):
        self.initdatabase()
        cursor = self.db.cursor()
        sql_get_train_num = "select trainNum from queryresult where id={};".format(id)
        train_num = cursor.execute(sql_get_train_num).fetchone()
        cursor.close()
        self.db.commit()
        self.db.close()
        return train_num


if __name__ == '__main__':
    querydb = QueryResultDB()
    querydb.initdatabase()