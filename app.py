from flask import Flask, render_template, request
import os
import psycopg2
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
username_db=os.getenv('USERNAME_DB')
password_db=os.getenv('PASSWORD_DB')


def conn_connection():
    conn = psycopg2.connect(
        host = 'localhost',
        database = 'flask_test',
        user = username_db,
        password = password_db
        )
    return conn

@app.route('/')
def jokes():
    conn = conn_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Jokes;')
    jokes = cur.fetchall() 
    cur.close()
    conn.close()
    return render_template('index.html', jokes=jokes)

@app.route('/add-joke', methods = ['GET', 'POST'])
def adding_joke():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        jokeText = request.form['jokeText']


        conn = conn_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO Jokes(title, author, jokeText)'
                    'VALUES(%s, %s, %s)',
                    (title, author, jokeText))
        conn.commit()
        cur.close()
        conn.close()

    return render_template('adding.html')



if __name__ == '__main__':
    app.run(debug=True)