# 简说

Python与MySQL之间有三条线:
1. DB API, 即数据库驱动、python模块, 使用python代码直接执行sql语句;
2. ORM, 如SQLAchemy, 将数据对象转换成SQL，然后使用数据API执行SQL并获取执行结果;
3. 另外DBUtils模块提供了一个数据库连接池，方便多线程场景中python操作数据库。

# 数据库驱动

1. MySQLdb. 也就是mysql-python, MySQLdb1太旧了,分出MySQLdb2时出现了**mysqlclient**;

2. **PyMySQL**. 纯python, mysqlclient和PyMySQL的维护者推荐使用**PyMySQL**

3. `mxODBC 和 mxODBC Connect. egenix家的东西;`

4. `pyodbc. 需进入http://code.google.com;`

5. **MySQL Connector**. Mysql Connector是MySQL的官方模块; 这个是纯python实现的MySQL接口, 由Oracle维护;使用MySQL API的全包python模块，没有C模块依赖项，只使用标准python模块。

6. mypysql. 由c语言实现, 目前还不能完全实现PEP249规范;

7. `PyPyODBC. 一看就知道支持PyPy;`

8. aiomysql,

9. **Mysqlclient**, mysqldb的fork, 迄今为止CPython最快的MySQL连接器。需要 C 库才能工作。`如果您想要更快的访问和重复访问，请坚持使用 mysqlclient`

# 优劣对比
1. mysql-python, 即MySQLdb, 是封装的mysqlclient,无法到底连接的socket. 
2. pymysql可以得到连接socket,却不能使用use_result语义.
3. 写入大量数据，上千万条的时候, pymysql好用一点, MySQL Connector会把内存吃的满满的
