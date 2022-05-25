from flask import Flask, render_template
from config import host, database, user, password
import psycopg2


import random

### Make the flask app
app = Flask(__name__)

### Routes

@app.route("/")
def browse():
     conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=database
)
     cursor = conn.cursor()
     cursor.execute('select id, date, title, content from entries order by date')
     rowlist = cursor.fetchall()

     return render_template('browse.html', entries=rowlist)



### Start flask
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True)