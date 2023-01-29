#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   one.py
@Time    :   2022/11/24 10:46:19
'''
import sqlalchemy as db
import pathlib


curdir = pathlib.Path(__file__).parent
engine = db.create_engine(f"sqlite:///{curdir}/one_database.sqlite")
conn = engine.connect()
metadata = db.MetaData()

# Student = db.Table(
#         "Student", metadata,
#         db.Column("ID", db.Integer(), primary_key = True),
#         db.Column("Name", db.String(255), nullable = False),
#         db.Column("Major", db.String(255), default = "Math"),
#         db.Column("Pass", db.Boolean(), default = True)
#     )
# metadata.create_all(engine)

Student = db.Table(
    "Student", metadata,
    autoload = True,
    autoload_with = engine
    )


# =========================================
# CRUD

# # 1 - insert
# # 1.1 - insert with a single term
# query = db.insert(Student).values(ID = "1", Name="Matthew", Major="English")
# # result = conn.execute(query)

# # 1.1 - insert with multiple terms
# query = db.insert(Student)
# values_list = [
#     {"ID": "2", "Name": "Nisha", "Major": "Science", "Pass": False},
#     {"ID": "3", "Name": "Natasha", "Major": "Chinese language", "Pass": True},
#     {"ID": "4", "Name": "Ben", "Major": "English", "Pass": False}
# ]
# conn.execute(query, values_list)


# # 2 - select
# query = Student.select()
# result = conn.execute(query).fetchall()

# print(result,"\n")
# print(repr(metadata.tables["Student"]), "\n")
# print(Student.columns.keys(), "\n")

# # 2.1 - advanced usage
# # 2.1.1 - where
# query = Student.select().where(Student.columns.Major=="English")
# output = conn.execute(query).fetchall()
# print(output)
# # 2.1.2 - and, or, not, in
# query_and = Student.select().where(db.and_(Student.columns.Major == "English", Student.columns.Pass != True))
# query_or = Student.select().where(db.or_(Student.columns.Major == "English", Student.columns.Pass != True))
# query_not = Student.select().where(db.not_(Student.columns.Pass != True))
# query_in = Student.select().where(Student.columns.Major.in_(["English", "Math"]))
# output = conn.execute(query_and).fetchall()
# print(output)

# # 2.1.3 - order by
# query_order_by = Student.select().order_by(db.desc(Student.columns.Name))
# print(conn.execute(query_order_by).fetchall())

# # 2.1.4 - limit
# query_limit = Student.select().limit(3)
# print(conn.execute(query_limit).fetchall())

# # 凡是不只是查找*的, 都用db.select而不是Student.select
# # 2.1.5 - sum, avg, count, min, max
# # select()括号里放东西, 要使用db., 而不是Student.
# query_func = db.select([db.func.sum(Student.columns.ID)])
# print(conn.execute(query_func).fetchall())

# # 2.1.6 - group by
# query_group_by = db.select([db.func.sum(Student.columns.ID), Student.columns.Major]).group_by(Student.columns.Pass)
# print(conn.execute(query_group_by).fetchall())

# # 2.1.7 - distinct
# query_distinct = db.select([Student.columns.Major.distinct()])
# print(conn.execute(query_distinct).fetchall())