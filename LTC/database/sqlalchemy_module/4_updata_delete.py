#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   4_updata_delete.py
@Time    :   2022/11/27 14:56:07
'''
import os
import sqlalchemy as db
import pandas as pd

class update_delete:
    def __init__(self) -> None:
        self.file_path = os.path.join(os.path.dirname(__file__), "0_multiple_table.sqlite")
        self.engine = db.create_engine(f"sqlite:///{self.file_path}")
        self.metadata = db.MetaData()
        self.st = db.Table("Student", self.metadata, autoload=True, autoload_with=self.engine)
        self.sc = db.Table("Score", self.metadata, autoload=True, autoload_with=self.engine)

    def virgin_view(self):
        try:
            conn = self.engine.connect()
            query = self.st.select()
            output = conn.execute(query).fetchall()
            df = pd.DataFrame(output)
            df.columns = output[0].keys()
            # print(result.fetchall())
            print("Student's virgin_view".ljust(40, "-"), "\n", df)
            
            query = self.sc.select()
            result = conn.execute(query)
            print("Score's virgin_view".ljust(40, "-"), "\n")
            for row in result:
                print(row)
        finally:
            result.close()
            conn.close()
    
    # def __repr__(self) -> str:
    #     return self.virgin_view()
        
    def one_update(self):
        try:
            conn = self.engine.connect()
            query = self.st.update().\
                values(s_Pass=True).\
                    where(self.st.columns.s_Name == "Ben")
            result = conn.execute(query)
        finally:
            result.close()
            conn.close()
        
    def after_update(self):
        try:
            conn = self.engine.connect()
            query = self.st.select()
            output = conn.execute(query).fetchall()
            df = pd.DataFrame(output)
            df.columns = output[0].keys()
            print(df)
            # print(self.conn.execute(query).fetchall())
        finally:
            conn.close()
    
    def one_delete(self):
        try:
            conn = self.engine.connect()
            query = self.st.delete().where(self.st.columns.s_Name == "Ben")
            result = conn.execute(query)
        finally:
            result.close()
            conn.close()
    
    def after_delete(self):
        return self.after_update()
        

if __name__ == "__main__":
    try:
        o = update_delete()
        o.virgin_view()
        o.one_update()
        o.after_update()
        o.one_delete()
        o.after_delete()
        o.engine.connect().close()
    finally:
        import sys
        sys.exit(0)
