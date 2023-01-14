#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   GM1_generate_test_file.py
@Time    :   2022/11/26 10:51:38
'''
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker


def preparation():
    import os, sys
    curdir = os.path.dirname(__file__)
    curdir = sys.argv[1]
    file_path = f"{curdir}\GM0_tb.sqlite"   # file_path = f"{curdir}/GM1_tb.sqlite"
    if os.path.exists(file_path):
        os.remove(file_path)
        
    global __engine, __metadata, __Base
    
    # engine = db.create_engine("mysql://jyeho:123456@localhost/fiftyq")   # 连接mysql
    # engine = db.create_engine("mysql+pymysql://jyeho:123456@localhost/fiftyq")    # 通过pymysql连接mysql
    __engine = db.create_engine(f"sqlite:///{file_path}")  # echo=True 是设置显示 SQLAlchemy 日志记录
    __metadata = db.MetaData()
    __Base = declarative_base()


def create_tb():
    global __engine, __metadata
    
    class Student(__Base):
        __tablename__ = "student"
        
        s_id = db.Column("s_id", db.Integer, primary_key  = True)
        s_name = db.Column("s_name", db.String(255), default = "-none-")
        s_major = db.Column("s_major", db.VARCHAR(255), default = "-none-")
        s_pass = db.Column("s_pass", db.Boolean, default = False)
        
        def __repr__(self) -> str:
            return f"<student info: (id = {self.s_id}, name = {self.s_name})>"
        
    class Score(__Base):
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
        "course", __metadata,
        db.Column("c_id", db.Integer, primary_key = True),
        db.Column("c_name", db.String(255), default = "-none-"),
        db.Column("t_id", db.Integer, default = "-none")
    )
    # 继承 Base 而建立的表结构必须用 Base.meta.create_all(engine) 来创建表
    # 使用 metadata 而建立的表结构必须用 meta.create_all(engine) 来创建表
    __Base.metadata.create_all(__engine)
    __metadata.create_all(__engine)
    
    
def bind_tb():
    global __engine, __metadata, _st, _sc, _co

    _st = db.Table("student", __metadata, autoload=True, autoload_with=__engine )
    _sc = db.Table("score", __metadata, autoload=True, autoload_with=__engine)
    _co = db.Table("course", __metadata, autoload=True, autoload_with=__engine)
    

def insert_data_with_session():
    """必须用create_tb()里的class"""
    global _st, _sc, _co
    
    Session = sessionmaker(bind=__engine)
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


def insert_data_with_conn():
    try:
        global _st, _sc, _co
        
        conn = __engine.connect()
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


def select_with_session():
    global _st, _sc, _co
    
    Session = sessionmaker(bind=__engine)
    session = Session()
    
    result = session.query(_st).all()
    sql = db.text("select * from student")

def main():
    preparation()
    create_tb()
    bind_tb()
    insert_data_with_conn()
    # insert_data_with_session()
    
if __name__ == "__main__":
    main()
    print(vars())
