from flask import Flask, render_template, g, request, redirect
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from os.path import join

app = Flask(__name__)
app.secret_key = "user_secret_key"

# database 

DATABASE = join('instance', 'user_login_data.db')

def get_db_connection():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

def get_cursor():
    db_connection = get_db_connection()
    return db_connection.cursor()

# def get_db_as_dict(cursor):
#     cursor.execute("SELECT * from user_login_data")
#     rows = cursor.fetchall()
#     rows = [dict(row) for row in rows]
#     return rows

def authenticate_user(email, password):
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM user_login_data WHERE email = ? LIMIT 1", (email,))
    user_detail = cursor.fetchone()


    if user_detail and email == user_detail['email']:
        is_valid = check_password_hash(user_detail['password'], password)
        if is_valid:
            name = user_detail['name']
            return name
        
def check_email_unique(email):
    cursor = get_cursor()
    cursor.execute("SELECT * FROM user_login_data WHERE email = ?", (email,) )
    user_detail = cursor.fetchone()
    cursor.close()

    if user_detail:
        return False
    else:
        return True
    
            
def add_user(name, email, password):
    prepped_data = (name, email, generate_password_hash(password))
    cursor = get_cursor()
    cursor.execute("INSERT INTO user_login_data (name, email, password) VALUES (?, ?, ?)", prepped_data)
    cursor.connection.commit()
    cursor.close()

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


@app.route("/register", methods=["GET","POST"])
def register():
    message = ""
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        password_re_enter = request.form.get('password_re_enter')
    
        if not name or not email or not password or not password_re_enter:
            return render_template("register.html", message="Incomplete fields")
        
        login_email_available = check_email_unique(email)

        if not login_email_available:
            return render_template("register.html", message="email as login ID not available")
        
        if login_email_available:
            add_user(name, email, password)
            return render_template("dashboard.html", name=name)

    return render_template("register.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
