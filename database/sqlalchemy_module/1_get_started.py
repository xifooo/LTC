#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   get_started.py
@Time    :   2022/11/23 19:25:47
'''

if __name__ == "__main__":
    import sqlalchemy as db
    from pathlib import Path
    
    curdir = Path(__file__).parent

    # 1 - 连接数据库
    engine = db.create_engine(f"sqlite:///{curdir}/0_mutiple_tb.sqlite")
    conn = engine.connect()
    metadata = db.MetaData()
    # 1.1 - 选择表
    Student = db.Table(
        "Student", metadata,
        autoload = True,
        autoload_with = engine
        )

    # - 打印“分区”元数据
    print(repr(metadata.tables["Student"]), "\n")
    # - 打印所有的列名
    print(Student.columns.keys(), "\n")


    # 2 - 查询
    query = Student.select()
    print(query)
    result = conn.execute(query).fetchall()
    print(result)
    # 2.1 - select
    query = Student.select()
    result = conn.execute(query).fetchall()
    print(result,"\n")
    
    # 2.2 - advanced usage
    # 2.2.1 - where
    query = Student.select().where(Student.columns.Major=="English")
    output = conn.execute(query).fetchall()
    print(output)
    
    # 2.2.2 - and, or, not, in
    query_and = Student.select().where(db.and_(Student.columns.Major == "English", Student.columns.Pass != True))
    query_or = Student.select().where(db.or_(Student.columns.Major == "English", Student.columns.Pass != True))
    query_not = Student.select().where(db.not_(Student.columns.Pass != True))
    query_in = Student.select().where(Student.columns.Major.in_(["English", "Math"]))
    output = conn.execute(query_and).fetchall()
    print(output)
    
    # 2.2.3 - order by
    query_order_by = Student.select().order_by(db.desc(Student.columns.Name))
    print(conn.execute(query_order_by).fetchall())
    
    # 2.2.4 - limit
    query_limit = Student.select().limit(3)
    print(conn.execute(query_limit).fetchall())
    
    # 凡是不只是查找*的, 都用db.select而不是Student.select
    # 2.2.5 - sum, avg, count, min, max
    # select()括号里放东西, 要使用db., 而不是Student.
    query_func = db.select([db.func.sum(Student.columns.ID)])
    print(conn.execute(query_func).fetchall())
    
    # 2.2.6 - group by
    query_group_by = db.select([db.func.sum(Student.columns.ID), Student.columns.Major]).group_by(Student.columns.Pass)
    print(conn.execute(query_group_by).fetchall())
    
    # 2.2.7 - distinct
    query_distinct = db.select([Student.columns.Major.distinct()])
    print(conn.execute(query_distinct).fetchall())
