#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   GM0_generate_test_file_OOP.py
@Time    :   2022/11/27 14:22:01
'''
import os
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class GM0_generate_test_file:
    def __init__(self) -> None:
        self.curdir = os.path.dirname(__file__)
        file_path = f"{self.curdir}/GM0_tb_OOP.sqlite"
        
        if os.path.exists(file_path):
            os.remove(file_path)
            
        self.engine = db.create_engine(f"sqlite:///{file_path}")
        self.metadata = db.MetaData()
        self.Base = declarative_base()
        
        class Student(self.Base):
            __tablename__ = "student"
            
            s_id = db.Column("s_id", db.Integer, primary_key  = True)
            s_name = db.Column("s_name", db.String(255), default = "-none-")
            s_major = db.Column("s_major", db.VARCHAR(255), default = "-none-")
            s_pass = db.Column("s_pass", db.Boolean, default = False)
            def __repr__(self) -> str:
                return f"<student info: (id = {self.s_id}, name = {self.s_name})>"
        
        class Score(self.Base):
            __tablename__ = 'score'
            
            s_id = db.Column("s_id", db.Integer)
            c_id = db.Column("c_id", db.Integer, default = 0)
            degree = db.Column("degree", db.VARCHAR(255), default = 0)
            
            __table_args__ = (
                db.PrimaryKeyConstraint("s_id","c_id"),
                {},
            )
            def __repr__(self) -> str:
                return f"<score info: (id = {self.s_id}, name = {self.c_id}, degree = {self.degree})>"
        
        Course = db.Table(
            "course", self.metadata,
            db.Column("c_id", db.Integer, primary_key = True),
            db.Column("c_name", db.String(255), default = "-none-"),
            db.Column("t_id", db.Integer, default = "-none")
        )
        # 继承 Base 而建立的表结构必须用 Base.meta.create_all(engine) 来创建表
        # 使用 metadata 而建立的表结构必须用 meta.create_all(engine) 来创建表
        self.Base.metadata.create_all(self.engine)
        self.metadata.create_all(self.engine)
    

    def insert_data_with_session(self):
        """必须与建表结构时的class交互"""
        Session = sessionmaker(bind=self.engine)
        session = Session()

        # commit_1 = Student(s_id = 1, s_name = "Matthew", s_major = "English", s_pass = True)
        # session.add(commit_1)
        # session.add(type(_st)(s_id = 1, s_name = "Matthew", s_major = "English", s_pass = True))
        session.add(Student(s_id = 1, s_name = "Matthew", s_major = "English", s_pass = True))
        session.commit()
        
        session.add_all([
            Student(s_id = 5, s_name = "jyeho", s_major = "Math", s_pass = True),
            Student(s_id = 2, s_name = "Nisha", s_major = "Science", s_pass = False),
            Student(s_id = 3, s_name = "Natasha", s_major = "Chinese language", s_pass = True),
            Student(s_id = 4, s_name = "Ben", s_major = "English", s_pass = False),
        ])
        session.commit()

    def insert_data_with_conn(self):
        try:
            _st = db.Table("student", self.metadata, autoload=True, autoload_with=self.engine)
            _sc = db.Table("score", self.metadata, autoload=True, autoload_with=self.engine)
            _co = db.Table("course", self.metadata, autoload=True, autoload_with=self.engine)
            
            conn = self.engine.connect()
            sentence = _st.insert().values(s_id=5, s_name="Jyeho", s_major="Math", s_pass=True)
            conn.execute(sentence)
            
            target = db.insert(_st)
            values_list = [
                {"s_id": "1", "s_name": "Matthew", "s_major": "English", "s_pass": True},
                {"s_id": "2", "s_name": "Nisha", "s_major": "Science", "s_pass": False},
                {"s_id": "3", "s_name": "Natasha", "s_major": "Chinese language", "s_pass": True},
                {"s_id": "4", "s_name": "Ben", "s_major": "English", "s_pass": False}
            ]
            conn.execute(target, values_list)

            target = db.insert(_sc)
            values_list_sc = [
                {"s_id": "2", "c_id": "1", "degree": "81"},
                {"s_id": "1", "c_id": "1", "degree": "100"},
                {"s_id": "1", "c_id": "2", "degree": "78"},
                {"s_id": "3", "c_id": "2", "degree": "92"},
                {"s_id": "4", "c_id": "1", "degree": "77"}
            ]
            conn.execute(target, values_list_sc)
            
            values_list_co = [
                {"c_id": "1", "c_name": "语文", "t_id": "2"},
                {"c_id": "2", "c_name": "数学", "t_id": "1"},
                {"c_id": "3", "c_name": "外语", "t_id": "3"}
            ]
            conn.execute(db.insert(_co), values_list_co)
        finally:
            conn.close()


if __name__ == "__main__":
    o = GM0_generate_test_file()
    o.insert_data_with_conn()
    
