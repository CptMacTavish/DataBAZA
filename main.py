from flask import Flask, render_template
from config import host, database, user, password
from datetime import datetime
import psycopg2


import random

### Make the flask app
app = Flask(__name__)




#first app вивід рандомного рядка в браузері



@app.route('/random')
def index1():

    array = ["Stanislav", "Matkovskyi", "KID-21"]

    random_thing = random.randrange(len(array))

    if (array[random_thing]) == "Stanislav":
        return "Hello, world!"
    elif (array[random_thing]) == "Matkovskyi":
        return "Stanislav"
    else:
        return (array[random_thing])




#templates вивід часу в браузер за допомогою файла html


@app.route("/time")
def index():
    timestring = datetime.now()
    return render_template("time.html", timestring=timestring)





# db1 занесення данних в таблицю з файлу schema.sql



conn = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cur = conn.cursor()
file = open("schema.sql", "r")
alltext = file.read()
cur.execute(alltext)
conn.commit()
cur.execute('SELECT * FROM entries')
designer = cur.fetchone()
cur.close()
conn.close()



# db3 вивід даних з таблиці в браузер


@app.route("/gym")
def dump_gymtable():
    conn = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
    cursor = conn.cursor()
    cursor.execute('select id, date, title, content from gymtable order by date')
    rows = cursor.fetchall()
    output = ""
    for r in rows:
        for el in r:

            output += str(el) + " " + "\t"
        output += "\n"
    return "<pre>" + output + "</pre>"




# db4 вивід в html файл


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