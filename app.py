from flask import Flask, render_template, g, request, redirect
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from os.path import join

app = Flask(__name__)

# database 

DATABASE = join('instance', 'user_login_data.db')

def get_db_connection():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

def get_db_as_dict(cursor):
    cursor.execute("SELECT * from user_login_data")
    rows = cursor.fetchall()
    rows = [dict(row) for row in rows]
    return rows

def authenticate_user(email, password):
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM user_login_data WHERE email=? LIMIT 1", (email,))
    user_detail = cursor.fetchone()


    if user_detail and email == user_detail['email']:
        is_valid = check_password_hash(user_detail['password'], password)
        if is_valid:
            name = user_detail['name']
            return name

@app.teardown_appcontext
def close_db_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# ------------

# routes
@app.route("/", methods=["GET"])
def home():
    message = "message placeholder"

    return render_template("home.html", message=message)

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return render_template("home.html", message="Incomplete email or password")
        return redirect("/")

    name = authenticate_user(email, password)
    if name is None:
        return render_template("home.html", message="user email not found or wrong password")
        return redirect("/")
    else:
        return render_template("dashboard.html", name=name)

    

if __name__ == "__main__":
    app.run(debug=True)
