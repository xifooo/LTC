# from sqlalchemy import create_engine, String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db

mysql_db = {
    'user': 'root',
    'passwd': '123456',
    'host': '127.0.0.1',
    'port': '3308'
}

# db_name = 'mysql+mysqlconnector://root:123456@localhost:3308/sqlalchemy_test'
db_name = f'mysql+pymysql://{mysql_db["user"]}:{mysql_db["passwd"]}@{mysql_db["host"]}:{mysql_db["port"]}/sqlalchemy_t'
engine = db.create_engine(db_name) # 1 - 连接数据库(创建连接池)


Base = declarative_base()   # 2 - 构造 declarative_base
class Student(Base):   # 2.1 继承Base ———— 建表，或者叫 model
    __tablename__ = 'student'   # table name
    # table structure
    s_id = db.Column("s_id", db.Integer, primary_key= True)
    s_name = db.Column("s_name", db.VARCHAR(255))
    s_major = db.Column("s_major", db.String(255), default= "")
    s_pass = db.Column("s_pass", db.Boolean, default= False)
    
    def __repr__(self) -> str:
        return f"<student info: (id = {self.s_id}, name = {self.s_name})>"
    
class Score(Base):
    __tablename__ = 'score'
    s_id = db.Column("s_id", db.Integer)
    c_id = db.Column("c_id", db.Integer, default= 0)
    degree = db.Column("degree", db.VARCHAR(255))
    
    __table_args__ = (
        db.PrimaryKeyConstraint('s_id', 'c_id'),
        {},
    )
    def __repr__(self) -> str:
        return f"<score info: (id = {self.s_id}, name = {self.s_name})>"
    

Base.metadata.create_all(engine)    # 2.1 建表
# db.MetaData.create_all(engine)

conn = sessionmaker(bind=engine)  # 3、创建session访问数据库
session = conn()  # (session 可类比 mysql.connector.connect.cursor() , 不同的是cursor执行的是sql语句, 还需要关闭)
