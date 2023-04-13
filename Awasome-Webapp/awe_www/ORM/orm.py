#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from ..utils.logger import logger
import aiomysql
from typing import Union, Optional
from .modelMeta import ModelMetaclass


async def createPool(loop, *args, **kwargs):
    logger.info("Creating database connection pool...")
    
    connectionConfig = {
        "host": kwargs.get("host", "localhost"),
        "port": kwargs.get("port", 3306),
        "user": kwargs.get("user"),
        "password": kwargs.get("password"),
        "db": kwargs.get("db"),
        "charset": kwargs.get("charset", "utf8mb4"),
        "autocommit": kwargs.get("autocommit", True),
        "maxsize": kwargs.get("maxsize", 10),
        "minsize": kwargs.get("minsize", 1),
        "loop": loop
    }
    global __pool
    __pool = await aiomysql.create_pool(**connectionConfig)
    
    
async def select(sql:str, args:Union[tuple, dict], size:Optional[int]=None) -> tuple:
    """
    select 参数化执行select语句
    
    Args:
        sql (str): 一个带参数的sql(占位符是“?“)
        args (Union[tuple, dict]): 一个要替换掉“?“的参数的tuple或dict
        size (Optional[int], optional): 指定返回数量size的记录. Defaults to None.
        
    Returns:
        tuple: 执行结果tuple
    """
    logger.info(sql, args)
    
    # global __pool
    async with __pool as conn:  # 异步上下文管理
        cur = await conn.cursor(aiomysql.DictCursor)
        await cur.execute(sql.replace("?", "%s"), args or ())  # sql的占位符是?, mysql的占位符是%s
        if size:
            result = await cur.fetchmany(size)
        else:
            result = await cur.fetchall()
        await cur.close()
        logger.info(f"rows returned: {len(result)}")
        return result
    # with (await __pool) as conn:  # 异步迭代（不推荐）
    #     cur = await conn.cursor(aiomysql.DictCursor)
    #     await cur.execute(sql.replace("?", "%s"), args or ())
    #     if size:
    #         result = await cur.fetchmany(size)
    #     else:
    #         result = await cur.fetchall()
    #     await cur.close()
    #     logger.info(f"rows returned: {len(result)}")
    #     return result

async def execute(sql:str, args:Union[tuple, dict]):
    logger.info(sql)
    
    async with __pool as conn:
        try:
            cur = await conn.cursor()
            await cur.execute(sql.replace("?", "%s"), args or ())
            affected = cur.rowcount  # 不能fetch()，只有结果数
            await cur.close()
        except BaseException as e:
            logger.error(e)
        return affected


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
    
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            # raise AttributeError(r"'Model' object has no attribute '%s'" % key)
            logger.error(f"Model object has no attribute {key}")

    def __setattr__(self, key, value):
        self[key] = value

    def getValue(self, key):
        return getattr(self, key, None)

    def getValueOrDefault(self, key):
        value = getattr(self, key, None)
        if value is None:
            field = self.__mappings__[key]
            if field.default is not None:
                value = field.default() if callable(field.default) else field.default
                logger.debug(f"using default value for {key}: {str(value)}")
                setattr(self, key, value)
        return value
    
    @classmethod
    async def findAll(cls, where=None, args=None, **kw):
        sql = [cls.__select__]
        
        if where:
            sql.append("where")
            sql.append(where)
        if args is None:
            args = []
        
        orderBy = kw.get("orderBy", None)
        if orderBy:
            sql.append("order by")
            sql.append(orderBy)
        
        limit = kw.get("limit", None)
        if limit is not None:
            sql.append("limit")
            if isinstance(limit, int):
                sql.append("?")
                args.append(limit)
            elif isinstance(limit, tuple) and len(limit) == 2:
                sql.append("?, ?")
                args.extend(limit)
            else:
                # raise ValueError(f"Invalid limit value: {str(limit)}")
                logger.error(f"Invalid limit value: {str(limit)}")
        result = await select(" ".join(sql), args=args)
        return [cls(**item) for item in result ]
    
    @classmethod
    async def findNum(cls, selectField, where=None, args=None):
        sql = [f"select {selectField} _num_ from {cls.__table__}"]
        if where:
            sql.append("where")
            sql.append(where)
        result = await select(" ".join(sql), args=args, size=1)
        if len(result) == 0:
            return None
        return result[0]["_num_"]
    
    @classmethod
    async def find(cls, pk):
        """
        find 返回符合指定查询条件（例如过滤条件和排序条件）的所有记录。

        Args:
            pk (_type_): _description_

        Returns:
            _type_: _description_
        """
        # result = await select(f"{cls.__select__, cls.__primary_key__} where `{[pk]} `")
        result = await select('%s where `%s`=?' % (cls.__select__, cls.__primary_key__), [pk], 1)
        if len(result) == 0:
            return None
        return cls(**result[0])
    
    async def save(self):
        args = list(map(self.getValueOrDefault, self.__fields__))
        args.append(self.getValueOrDefault(self.__primary_key__))
        rows = await execute(self.__insert__, args)
        if rows != 1:
            logger.warning('failed to insert record: affected rows: %s' % rows)

    async def update(self):
        args = list(map(self.getValue, self.__fields__))
        args.append(self.getValue(self.__primary_key__))
        rows = await execute(self.__update__, args)
        if rows != 1:
            logger.warning('failed to update by primary key: affected rows: %s' % rows)

    async def remove(self):
        args = [self.getValue(self.__primary_key__)]
        rows = await execute(self.__delete__, args)
        if rows != 1:
            logger.warning('failed to remove by primary key: affected rows: %s' % rows)
"""      
好的，下面是这段代码中 Model 类中定义的每个函数做了什么事情的详细说明：

__init__(self, **kw)

此方法是 Model 类的构造函数。
它通过调用 super(Model, self).__init__(**kw) 初始化基类 dict。
**kw 参数接收字段及其值，然后将它们存储到 Model 对象中，以便能够进行数据操作。
__getattr__(self, key)

此方法为获取属性而提供支持。
如果传递的键不存在于 Model 对象中，会输出日志信息并返回空值。
__setattr__(self, key, value)

此方法用于设置属性。
它将传递的值与设置的键相关联并存储在 Model 对象中。
getValue(self, key)

此方法返回与键关联的当前数据值。
如果找不到值，则返回空值。
getValueOrDefault(self, key)

此方法与 getValue 相似，但用于获取指定字段的默认值。
如果找不到值，方法会返回默认值，而不是空值。
findAll(cls, where=None, args=None, **kw)

此方法返回符合指定查询条件（例如过滤条件和排序条件）的所有记录。
方法使用 __select__ 属性构建查询字符串，然后使用 select 函数执行该查询，从而返回所有符合条件的数据对象。
args 参数是要传递给 select 函数的顺序参数列表。
**kw 参数用于传递其他可选查询条件，例如 orderBy 和 limit（也可以不提供）。
findNum(cls, selectField, where=None, args=None)

此方法返回计算所得的符合指定条件的数据记录数。
此方法首先构建一个选择计数的查询字符串，然后执行计数查询，将结果存储在 _num_ 一列中返回。
find(cls, pk)

此方法根据给定的主键值查找数据库中的记录。
它使用 __select__ 属性构建选择字符串、将给定的主键值用于约束查找、再通过 select 函数执行查找过程。
如果找到符合条件的数据，则将它转换为 Model 对象并返回结果。否则返回空值。
save(self)

此方法将当前 Model 对象的数据保存到数据库中。
它首先使用 getValueOrDefault 方法获取当前对象所有已定义字段的值，然后将它们放入一个列表中。接着调用 getValueOrDefault 方法获取主键字段的值，并将其追加到上述列表中。然后调用 execute 函数并将此列表和代表插入数据库语句的 __insert__ 属性作为参数传递给该函数。如果返回的影响行数不等于1，则输出警告信息。
update(self)

此方法用于将当前 Model 对象的数据更新到数据库中。
此方法与 save 方法相似，但它使用 getValue 方法获取当前对象的字段值，而不是默认值。然后调用 execute 函数并将此列表和代表更新数据库语句的 __update__ 属性作为参数传递给该函数。如果返回的影响行数不等于1，则输出警告信息。
remove(self)

此方法用于从数据库中删除当前 Model 对象。
它使用 getValue 方法获取当前对象的主键字段值，构建对应的删除命令字符串（__delete__ 属性），并将其与主键值一起传递给 execute 函数进行删除。如果返回的影响行数不等于1，则输出警告信息。
"""