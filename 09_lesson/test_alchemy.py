from sqlalchemy import create_engine
from sqlalchemy.sql import text
db_connection_sting = "postgresql://postgres:2025@localhost:5432/QA"



def test_db_connection():
      db = create_engine(db_connection_sting)
      db.table_names()



def test_insert():
      db = create_engine(db_connection_sting)
      sql= text("insert  into student user_id" "education_form values ('1255','group')")
      db.delete('1255','group')

def test_update():
      db = create_engine(db_connection_sting)
      sql = text("insert  into student user_id" "education_form values ('1255','group')")
      sql = text("update student set education_form = 'null' where user_id = 1255)")
      db.delete('1255','null')


def test_delete():
      db = create_engine(db_connection_sting)
      sql = text("insert  into student user_id" "education_form values ('1255','group')")
      sql = text(" delete from student where user_id = 1255")
