#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from ..utils.logger import logger
from fields import Field


class ModelMetaclass(type):
    '''
    任何继承自 Model 的类(比如 User),
    会自动通过 ModelMetaclass 扫描映射关系,
    并存储到自身的类属性如 __table__、__mappings__ 中。
    '''
    # 在实现__new__方法时，需要注意传入的参数包括cls(当前类)、name(类名)、bases(父类)和attrs(属性字典)。
    # 同时，在创建类对象时，可能需要对类名、属性等进行处理。
    def __new__(cls, name:str, base, attrs:dict): 
        # 排除 Model 类本体
        if name == "Model":
            return type.__new__(cls, name, base, attrs)
        # 获取 table 名字
        tableName = attrs.get("__table__", None) or name
        logger.info(f"found model:{name} (table: {tableName})")
        # 获取 table 的所有 Field 和主键名
        mappings, fields, pk = {}, [], None
        for k, v in attrs.items():
            if isinstance(v, Field):
                logger.info(f"found mapping: {k} ::: {v}")
                mappings[k] = v
                if v.primary_key:
                    if pk:
                        logger.error(f"Duplicate primary key for field: {k}")
                        # raise RuntimeError(f"Duplicate primary key for field: {k}")
                    pk = k
                else:
                    fields.append(k)
        if not pk:
            raise RuntimeError(f"Primary key not found")
        for k in mappings.keys():
            attrs.pop(k)
        escaped_fields = list(map(lambda x: f'`{x}`' , fields))   #############################
        attrs["__mappings__"] = mappings
        attrs["__table__"] = tableName
        attrs["__primary_key__"] = pk
        attrs["__fields__"] = fields
        
        attrs["__select__"] = f"select `{pk}`, {', '.join(escaped_fields)} from `{tableName}`"
        attrs["__insert__"] = f"insert into `{tableName}` ({', '.join(escaped_fields)}, `{pk}`) values {create_args_string(len(escaped_fields) + 1)} "
        attrs['__update__'] = f"update `{tableName}` set {', '.join(map(lambda f: f'`{(mappings.get(f).name or f)}`=?', fields))} where `{pk}`=?"
        attrs['__delete__'] = f"delete from `{tableName}` where `{pk}`=?"
        # attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (tableName, ', '.join(escaped_fields), pk, create_args_string(len(escaped_fields) + 1))
        # attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (tableName, ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), pk)
        # attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (tableName, pk)

def create_args_string(num):
    return ", ".join(["?" for i in range(num)])
