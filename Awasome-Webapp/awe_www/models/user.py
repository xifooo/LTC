#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from ..ORM.orm import Model
from ..ORM.fields import StringField, BooleanField, IntegerField, FloatField, TextField

class User(Model):
    __table__ = "users"
    
    id = IntegerField(primary_key=True)
    name = StringField()
    
    
u = User(id="1101", name="Jyeeho")
u.insert()

query = User.findAll()
query = User.findNum()

class Blog(Model):
    __table__ = "blogs"
    
    id = IntegerField(primary_key=True)
    name = StringField()