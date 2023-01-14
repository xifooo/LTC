#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   3_csv_to_sql.py
@Time    :   2022/11/25 13:58:02
'''
import sqlalchemy as db
import pandas as pd
from pathlib import Path


class Csv_to_sql:
    def __init__(self) -> None:
        self.curdir = Path(__file__).parent
        self.engine = db.create_engine(f"sqlite:///{self.curdir}/3_csv_to_sql.sqlite")
        self.df = pd.read_csv(f"{self.curdir}/2_output.csv")
        
    def to_sql(self):
        #  s_Major 为 English 且 选择了 c_ID 为 2 的所有列
        self.df.to_sql(con = self.engine, name = "first_tb", if_exists = 'replace', index = False)
        
    def check_up(self):
        try:
            # 验证
            conn = self.engine.connect()
            metadata = db.MetaData()
            obj_t = db.Table('first_tb', metadata, autoload=True, autoload_with=self.engine)
            query = obj_t.select()
            result = conn.execute(query).fetchall()
            for line in result:
                print(line)
        finally:
            conn.close()


if __name__ == "__main__":
    o = Csv_to_sql()
    o.to_sql()
    o.check_up()


