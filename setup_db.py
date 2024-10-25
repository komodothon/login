import sqlite3
from werkzeug.security import generate_password_hash
from os.path import join

DATABASE = join('instance', 'user_login_data.db')

sample_user_data = [
    {
        'email': 'user1@sample.com',
        'name': 'Name1',
        'password': 'Hellouser1'
    },
        {
        'email': 'user2@sample.com',
        'name': 'Name2',
        'password': 'Hellouser2'
    },
        {
        'email': 'user3@sample.com',
        'name': 'Name3',
        'password': 'Hellouser3'
    },
        {
        'email': 'user4@sample.com',
        'name': 'Name4',
        'password': 'Hellouser4'
    }

]

def create_db_and_table():
    db_connection = sqlite3.connect(DATABASE)
    cursor = db_connection.cursor()
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS user_login_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            email TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            password TEXT NOT NULL)
        """
    )
    db_connection.commit()
    db_connection.close()


def insert_sample_data():

    prepped_data = [
        (user_detail['email'], user_detail['name'], 
         generate_password_hash(user_detail['password']))
           for user_detail in sample_user_data
    ]       

    db_connection = sqlite3.connect(DATABASE)
    cursor = db_connection.cursor()
    cursor.executemany("INSERT INTO user_login_data (email, name, password) VALUES (?,?,?)", prepped_data)
    db_connection.commit()
    db_connection.close()
    
if __name__ == "__main__":
    create_db_and_table()
    insert_sample_data()