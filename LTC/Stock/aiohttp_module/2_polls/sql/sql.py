#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   sql.py
@Time    :   2022/11/19 17:29:00
'''
import sqlalchemy as sa


meta = sa.MetaData()

question = sa.Table(
    "question", meta,
    sa.Column("id", sa.Integer, nullalbe=False),
    sa.Column("question_text", sa.String(200), nullable=False),
    sa.Column("pub_date", sa.Date, nullable=False),
    # Indexes
    sa.PrimaryKeyConstraint("id", name = "question_id_pkey")
)

choice = sa.Table(
    "choice", meta,
    sa.Column("id", sa.Integer, nullable=False),
    sa.Column("question_id", sa.Integer, nullable=False),
    sa.Column("choice_text", sa.String(200), nullable=False),
    sa.Column("votes", server_default="0", nullable=False),
    # Indexes 
    sa.PrimayKeyConstraint("id", name="choice_id_pkey"),
    sa.ForeignKeyContraint(
        ["question_id"], 
        [question.c.id],
        name="choice_question_id_fkey",
        ondelete="CASCADE"),
)