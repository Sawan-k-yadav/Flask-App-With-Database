## To create database and tables from the database uri model for the first time only

# from app import app, db

# with app.app_context():
#     if not db.reflect():
#         db.create_all()


import pymysql


# Creating database
def create_database():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='sawan',
        port=3306
    )
    cursor = conn.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS todo;')
    conn.close()

## for creating table
def create_tables():
    from app import app, db
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    create_database()
    create_tables()