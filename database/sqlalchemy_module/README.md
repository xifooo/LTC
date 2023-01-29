# sqlalchemy简述
+ 从逻辑关系上讲，pymysql、sqlite3 这些使 python 与数据库交互的驱动与 sqlalchemy 所处地位一样，并且它们的主要功能也几乎一致。
+ sqlalchemy 采用了 OOP 的思想，这是与python数据库驱动最大的本质区别。
+ sqlalchemy 也兼容原生sql。

# session OR conn
```python
import sqlalchemy as db
engine = db.create_engine("sqlite:///GM0_tb.sqlite")
# session
Session = db.orm.sessionmaker(bing=engine)
session = Session()
# conn
conn = engine.connect()
```
> 当调用 Engine.execute（） 或 Engine.connect（） 等方法时，引擎会建立与数据库的真正 DBAPI 连接。然后，它用于发出不直接使用引擎的 SQLORM;相反，它由ORM在幕后使用。
session必须与建表结构时的class交互，比conn能实现更多数据库功能如rollback、flush等
1. session执行完需要commit，conn在程序结束时需要close
2. session更适合sqlalchemy内嵌于一个项目中时使用，而conn都可以
# SQLite
> SQLite是一个非常轻量级的版本。它一次只能执行一个功能。当前，它正在执行选择查询。我们需要在删除表之前关闭所有执行。
关闭所有的conn.execute()的执行结果