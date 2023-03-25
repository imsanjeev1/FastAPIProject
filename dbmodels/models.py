from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from configuration.db_connect import meta

words=Table(
    'words',meta,
    Column('id',Integer,primary_key=True),
    Column('input_word',String(200)),
    Column('converted_word',String(200)),
    Column('language_type',String(200)),
)