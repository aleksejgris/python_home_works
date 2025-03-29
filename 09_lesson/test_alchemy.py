from sqlalchemy import create_engine
from sqlalchemy.sql import text
db_connection_sting = "postgresql://postgres:2025@localhost:5432/QA"



def test_db_connection():
      db = create_engine(db_connection_sting)
      db.table_names()



def test_insert():
            db = create_engine(db_connection_sting)
            with db.connect() as conn:

                  conn.execute(text("INSERT INTO student (user_id, education_form) VALUES (:new_id, :new_form)"),
                               {"new_id": 1255, "new_form": "group"})
                  conn.commit()

                  result = conn.execute(text("SELECT * FROM student WHERE user_id = :new_id"),
                                        {"new_id": 1255}).fetchone()
                  assert result is not None, "Данные не добавлены"


def test_update():
            db = create_engine(db_connection_sting)
            with db.connect() as conn:

                  conn.execute(text("UPDATE student SET education_form = :new_form WHERE user_id = :user_id"),
                               {"new_form": "null", "user_id": 1255})
                  conn.commit()

                  result = conn.execute(text("SELECT education_form FROM student WHERE user_id = :user_id"),
                                        {"user_id": 1255}).fetchone()
                  assert result[0] == "null", "Данные не обновлены"



def test_delete():
            db = create_engine(db_connection_sting)
            with db.connect() as conn:

                  conn.execute(text("DELETE FROM student WHERE user_id = :user_id"), {"user_id": 1255})
                  conn.commit()

                  result = conn.execute(text("SELECT * FROM student WHERE user_id = :user_id"),
                                        {"user_id": 1255}).fetchone()
                  assert result is None, "Данные не удалены"

