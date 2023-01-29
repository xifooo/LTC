#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   output_to_df.py
@Time    :   2022/11/24 21:25:11
'''
from pathlib import Path

import sqlalchemy as db
import pandas as pd

class Output_to_df:
    def __init__(self) -> None:
        self.curdir = Path(__file__).parent
        engine = db.create_engine(f"sqlite:///{self.curdir}/0_multiple_tb.sqlite")
        self.conn = engine.connect()

        metadata = db.MetaData()
        self.Student = db.Table(
            "Student", metadata,
            autoload = True,
            autoload_with = engine
            )
        self.Score = db.Table(
            "Score", metadata,
            autoload = True,
            autoload_with = engine
        )
        
    def simple_select(self):
        query = self.Student.select().where(self.Student.columns.s_Major.in_(["English", "Math"]))
        output = self.conn.execute(query).fetchall()

        # 将查询结果转化为 pandas 里的 dataframe
        self.data = pd.DataFrame(output)
        self.data.columns = output[0].keys()
        return self.data

    def complex_select(self):
        # 复杂查询
        # s_ID 为两张表的公共列, 选择 s_Major 为 English 且 选择了 c_ID 为 2 的所有列
        query_sql = "select * from Student inner join Score on Student.s_ID = Score.s_ID where Student.s_Major='English' and Score.c_ID = 2 "

        # ? 下方query语句有问题
        # query = db.select([Student, Score].\
        #     select_from(Student.join(Score, Student.columns.s_ID == Score.columns.s_ID))).\
        #         where(db.and_(Student.columns.s_Major == "English", Score.columns.c_ID == "2")).\
        #             order_by(Student.s_ID)

        output = self.conn.execute(query_sql).fetchall()

        self.data = pd.DataFrame(output)
        self.data.columns = output[0].keys()
        return self.data

    def to_csv(self):
        data = self.complex_select()
        # 最后通过 df 的 to_csv() 将结果存储为csv格式文件
        data.to_csv(f"{self.curdir}/2_output.csv", index = False)
        del data


if __name__ == "__main__":
    try:
        o = Output_to_df()
        
        print("simple_select".ljust(20, "-"), "\n", o.simple_select())
        
        print("complex_select".ljust(20, "-"), "\n", o.complex_select())
        
        o.to_csv()
        
        print(o.__dict__)
        
    finally:
        o.conn.close()