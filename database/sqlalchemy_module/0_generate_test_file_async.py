#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   generate_test_file.py
@Time    :   2022/11/24 21:32:55
'''
from pathlib import Path
import sqlalchemy as db
import os, asyncio


async def check():
    # file_path = file_path.as_posix()
    # assert file_path == "f:/LTC/LTC/database/sqlalchemy_module/multiple_tb.sqlite"
    curdir = Path(__file__).parent
    file_path = curdir / "0_multiple_tb.sqlite"
    
    if file_path.exists():
        os.remove(file_path)
    return file_path
    
    
async def main():
    task = asyncio.create_task(check())
    file_path = await task
    
    engine = db.create_engine(f"sqlite:///{file_path}")
    conn = engine.connect()
    metadata = db.MetaData()
    Student = db.Table(
            "Student", metadata,
            db.Column("s_ID", db.Integer(), primary_key = True),
            db.Column("s_Name", db.String(255), nullable = False),
            db.Column("s_Major", db.String(255), default = " "),
            db.Column("s_Pass", db.Boolean(), default = False)
        )
    Score = db.Table(
            "Score", metadata,
            db.Column("s_ID", db.Integer(), default = 0),
            db.Column("c_ID", db.Integer(), nullable = False),
            db.Column("degree", db.Integer(), default = 0)
        )
    metadata.create_all(engine)
    
    # 插入记录
    query = db.insert(Student).values(s_ID="5",s_Name="Jyeho", s_Major="Math", s_Pass=True)
    query = db.insert(Student)
    values_list = [
        {"s_ID": "1", "s_Name": "Matthew", "s_Major": "English", "s_Pass": True},
        {"s_ID": "2", "s_Name": "Nisha", "s_Major": "Science", "s_Pass": False},
        {"s_ID": "3", "s_Name": "Natasha", "s_Major": "Chinese language", "s_Pass": True},
        {"s_ID": "4", "s_Name": "Ben", "s_Major": "English", "s_Pass": False}

    ]
    conn.execute(query, values_list)
    
    query = db.insert(Score)
    values_list = [
        {"s_ID": "2", "c_ID": "1", "degree": "81"},
        {"s_ID": "1", "c_ID": "1", "degree": "100"},
        {"s_ID": "1", "c_ID": "2", "degree": "78"},
        {"s_ID": "3", "c_ID": "2", "degree": "92"},
        {"s_ID": "4", "c_ID": "1", "degree": "77"}
    ]
    # conn.execute(query, values_list)
    conn.execute(Score.insert(), values_list)


# async def main():
#     try:
#         file_path = await check()
#         engine = db.create_engine(f"sqlite:///{file_path}")
#         conn = engine.connect()
#         metadata = db.MetaData()
#         Student = db.Table(
#                 "Student", metadata,
#                 db.Column("s_ID", db.Integer(), primary_key = True),
#                 db.Column("s_Name", db.String(255), nullable = False),
#                 db.Column("s_Major", db.String(255), default = " "),
#                 db.Column("s_Pass", db.Boolean(), default = False)
#             )
#         Score = db.Table(
#                 "Score", metadata,
#                 db.Column("s_ID", db.Integer(), default = 0),
#                 db.Column("c_ID", db.Integer(), nullable = False),
#                 db.Column("degree", db.Integer(), default = 0)
#             )
#         metadata.create_all(engine)
        
#         # 插入记录
#         query = db.insert(Student).values(s_ID="5",s_Name="Jyeho", s_Major="Math", s_Pass=True)
#         query = db.insert(Student)
#         values_list = [
#             {"s_ID": "1", "s_Name": "Matthew", "s_Major": "English", "s_Pass": True},
#             {"s_ID": "2", "s_Name": "Nisha", "s_Major": "Science", "s_Pass": False},
#             {"s_ID": "3", "s_Name": "Natasha", "s_Major": "Chinese language", "s_Pass": True},
#             {"s_ID": "4", "s_Name": "Ben", "s_Major": "English", "s_Pass": False}

#         ]
#         conn.execute(query, values_list)
        
#         query = db.insert(Score)
#         values_list = [
#             {"s_ID": "2", "c_ID": "1", "degree": "81"},
#             {"s_ID": "1", "c_ID": "1", "degree": "100"},
#             {"s_ID": "1", "c_ID": "2", "degree": "78"},
#             {"s_ID": "3", "c_ID": "2", "degree": "92"},
#             {"s_ID": "4", "c_ID": "1", "degree": "77"}
#         ]
#         # conn.execute(query, values_list)
#         conn.execute(Score.insert(), values_list)
#     finally:
#         conn.close()

async def use_sqlite3():
    try:
        import sqlite3
        file_path = await check()
            
        conn = sqlite3.connect(f"{file_path}")
        cursor = conn.cursor()
        
        cursor.execute("""create table `Student`(
            `s_ID` varchar(255) primary key, 
            `s_Name` varchar(255)),
            `s_Major` varchar(255) default '',
            `s_Pass` boolean default False)
            """)
        cursor.execute("""create table `Score`(
            `s_ID` varchar(255) not null, 
            `c_ID` varchar(255), 
            `degree` varchar(255) default 0)
            """)
        
        cursor.execute("insert into Student values('1', 'Matthew', 'English', True)")
        cursor.execute("insert into Student values('?', '?', '?', ?)",("2", "Nisha", "Science", "False"))
        cursor.execute("insert into Student values('?', '?', '?', ?)",("3", "Natasha", "Chinese language", "True"))
        cursor.execute("insert into Student values('?', '?', '?', ?)",("4", "Ben", "English", "False"))
        
        conn.commit()
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    asyncio.run(main())
    
