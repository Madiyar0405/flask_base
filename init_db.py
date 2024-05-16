import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

username_db=os.getenv('USERNAME_DB')
password_db=os.getenv('PASSWORD_DB')


conn = psycopg2.connect(
    host = 'localhost',
    database = 'flask_test',
    user = username_db,
    password = password_db
)


cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Jokes;')
cur.execute('CREATE TABLE Jokes(id SERIAL PRIMARY KEY,'
            'title varchar(255) NOT NULL,'
            'author varchar(50) NOT NULL,'
            'jokeText text,'
            'date_added date DEFAULT CURRENT_TIMESTAMP);')


cur.execute('INSERT INTO Jokes(title, author, jokeText)'
            'VALUES (%s, %s, %s)',
            ('О числах Фибоначчи',
             'Студент Аиту',
             'Эта шутка про числа Фибоначчи дажу хуже, чем предыдущие две вместе взятые')
            )


conn.commit()

cur.close()
conn.close()