#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   get_started.py
@Time    :   2022/11/23 19:25:47
'''
import sqlalchemy as db

# def select(tb_obj, conn):
#     query = tb_obj.select()
#     exe = conn.execute(query)
#     result = exe.fetchmany(5)    # fetchone, fetchmany, fetchall
#     return result

if __name__ == "__main__":
    # 1
    engine = db.create_engine("sqlite:///get-started.sqlite")
    conn = engine.connect()
    
    # 2.1 - extracting the metadata
    metadata = db.MetaData()
    
    # 2.2 - Table object, needing table name and metadata
    division = db.Table("divisions", 
                        args=metadata,
                        autoload = True,
                        autoload_with = engine)
    # ========================================
    # 3
    Student = db.Table(
        "Student", metadata,
        db.Column("ID", db.Integer(), primary_key = True),
        db.Column("Name", db.String(255), nullable = False),
        db.Column("Major", db.String(255), default = "Math"),
        db.Column("Pass", db.Boolean(), default = True)
    )
    
    metadata.create_all(engine)
    
    # =========================================
    # 4 CRUD
    # 4.1 - insert with a single term
    query = db.insert(Student).values(ID=1, Name="Matthew", Major="English")
    result = conn.execute(query)
    # 4.1 - insert with multiple terms
    query = db.insert(Student)
    values_list = [
        {"ID": "2", "Name": "Nisha", "Major": "Science", "Pass": False},
        {"ID": "3", "Name": "Natasha", "Major": "Chinese language", "Pass": True},
        {"ID": "4", "Name": "Ben", "Major": "English", "Pass": False}
    ]
    conn.execute(query, values_list)
    
    # 4.2 - select 
    output = conn.execute(Student.select()).fetchall()
    print(output)
    # 4.2 - select with SQL
    output_sql = conn.execute("select * from Student").fetchall()
    print(output_sql)
    
    # 4.3 - update
    query = Student.update().values(Pass=True).where(Student.columns.Name =="Nisha")
    conn.execute(query)
    
    # ===========================================
    # 5 advanced usage
    # 5.1 - where
    query = Student.select().where(Student.columns.Major=="English")
    output = conn.execute(query).fetchall()
    print(output)
    # 5.2 - and, or, not
    query = Student.select().where(db.and_(Student.columns.Major == "English", Student.columns.Pass != True))
    query = Student.select().where(db.or_(Student.columns.Major == "English", Student.columns.Pass != True))
    query = Student.select().where(db.not_(Student.columns.Major == "English", Student.columns.Pass != True))
    output = conn.execute(query).fetchall()
    print(output)
    # 5.3 - order by
    query = Student.select().order_by(db.desc(Student.columns.Name))
    # 5.4 - limit
    query = Student.select().limit(3)
    # 5.5 - sum, avg, count, min, max
    query = Student.select([db.func.sum(Student.columns.ID)])
    # 5.6 - group by
    query = Student.select([db.func.sum(Student.columns.ID),Student.columns.Major]).group_by(Student.columns.Pass)
    # 5.7 - distinct
    query = Student.select([Student.columns.Major.distinct()])
    # 5.7 - in
    query = Student.select().where(Student.columns.Major.in_(["English", "Math"]))
    
    # ==============================================
    # 6