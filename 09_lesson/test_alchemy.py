from sqlalchemy import create_engine
from sqlalchemy.sql import text
db_connection_sting = "postgresql://postgres:2025@localhost:5432/QA"



def test_db_connection():
      db = create_engine(db_connection_sting)
      db.table_names()



def test_insert():
      db = create_engine(db_connection_sting)
      sql= text("INSERT  INTO student user_id" "education_form VALUES ('1255','group')")
      db.execute(sql,new_id = 1255,new_form ='group')

def test_update():
      db = create_engine(db_connection_sting)
      sql = text("INSERT  INTO student user_id" "education_form VALUES ('1255','group')")
      sql = text("update student set education_form = 'null' where user_id = 1255")
      db.execute(sql,education_form = 'null',user_id =1255 )


def test_delete():
      db = create_engine(db_connection_sting)
      sql = text("INSERT  INTO student user_id" "education_form VALUES ('1255','group')")
      sql = text(" delete from student where user_id = 1255")
      db.execute(sql,user_id = 1255)
