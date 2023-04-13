#!/usr/bin/env python
# -*- encoding: utf-8 -*-

class Field:
    def __init__(self, name, column_type, primary_key, default) -> None:
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default
    
    def __str__(self) -> str:
        return f"<{self.__class__.__name__}, {self.column_type}:{self.name}>"

class StringField(Field):
    def __init__(self, name=None, primary_key=False, default=None, ddl="varchar(100)") -> None:
        super().__init__(name, ddl, primary_key, default)
        
class BooleanField(Field):
    def __init__(self, name=None, default=False) -> None:
        super().__init__(name, "boolean", False, default)
        
class IntegerField(Field):
    def __init__(self, name=None, primary_key=False, default=0) -> None:
        super().__init__(name, "bigint", primary_key, default)
        
class FloatField(Field):
    def __init__(self, name=None, primary_key=False, default=None) -> None:
        super().__init__(name, "real", primary_key, default)
        
class TextField(Field):
    def __init__(self, name=None, default=None) -> None:
        super().__init__(name, "text", False, default)