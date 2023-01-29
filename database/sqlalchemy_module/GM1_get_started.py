#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   GM2_get_started.py
@Time    :   2022/11/26 16:47:11
'''
import sqlalchemy as db
import os


curdir = os.path.dirname(__file__)
file_path = f"{curdir}/GM0_tb.sqlite"
engine = db.create_engine(f"sqlite:///{file_path}")
engine_mysql = db.create_engine(f"mysql+pymysql://jyeho:123456@localhost/GM0_tb")
# dialect+driver://username:password@host:port/database

class CRUD:
    def __init__(self) -> None:
        self.conn = engine.connect()
        ...
        
    def select(self, key="all"):
        try:
            if key == "all":
                sql_text_select_all = db.text("select * from :tb_name")
                result = self.conn.execute(sql_text_select_all, tb_name = "student")
                for row in result:
                    print(row)
            elif key == "where":
                sql_text_select_where = db.text("select * from :tb_name where :tail")
                result = self.conn.execute(sql_text_select_where, tb_name = "student", tail = "student.s_pass is True")
                for row in result:
                    print(row)
        finally:
            result.close()


if __name__ == "__main__":
    # 1 - engine.table_names()
    insp = db.inspect(engine)
    print(insp.get_table_names())
    # print(engine.table_names())  # sqlalchemy 1.4 以后就废除了
    
    # 2 - engine.dispost()
    engine.dispose()
    
    # 3 - engine.begin()
    # 返回一个上下文管理器，它传递一个已建立事务的连接。一旦操作成功，事务将被提交，否则将被回滚
    with engine.begin() as session:
        result = session.execute("select * from student")
        for row in result:
            print(row)
            
    # # 4 - engine.driver()
    # print(engine_mysql.driver())
    
    # 5 - engine.transaction()
    # 事务()在事务边界内执行给定的函数
    def func():
        ...
    engine.transaction(func)
    
