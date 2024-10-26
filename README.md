# Login

## Overview of the Project
1. To set up a flask web application to make a user registration and login gateway and then lead to a dashboard page.


## Tools employed
1. Python, flask, html, css, sqlite

## Deployment
Currently deployed at https://user-login-and-registration.onrender.com

## Code Structure


- **`login/`**: Contains all source code files.
  - **`App.py`**: Flask application
  - **`setup_db.py`**: Setup of database with sample data. (run this first - one time to setup the database)
  
- **`instance/`**: Instance folder contains the database file
  - **`user_login_data.db`**: Database file holding information.

- **`templates/`**: HTML files that are served directly.
  - **`layout.html`**: Layout template for alll html files. 
  - **`home.html`**: Landing page HTML file.
  - **`register.html`**: New user registration HTML file.
  - **`dashboard.html`**: Dashboard page HTML file.

- **`static/`**: Contains static files.
  - **`css/`**: Contains CSS files for styling.
    - **`styles.css`**: Main stylesheet.
  - **`image/`**: Folder with image(s)
    - **`sample_data.jpg`**: sample user data shown for testing out the app.

- **`.gitignore`**: Specifies files and directories that should be ignored by Git.
- **`README.md`**: Documentation file for the project.

## Code breakdown

### app.py
--------- database related operations and functions --------

**def get_db_connection()**: to setup a database connection. guideline from chatgpt

**def get_cursor()**: function calls the get_db_connection and then returns a cursor which can be used to execute sqlite commands

**def authenticate_user(email, password)**: user - login. authenticates a provided login detail against what's in the database

**def check_email_unique(email)**: during user registration, checks against the database if a provided email is available to be used as unique login email and returns True or False

**def add_user(name, email, password)**: New user registration. after unique email id availability check, this function adds the new user details into the database

**@app.teardown_appcontext**
**def close_db_connection(exception)**: closes database connection connection after every request

------- routes ---------

**@app.route("/", methods=["GET"])**
**def home():** : landing page. GET method loads home.html

**@app.route("/login", methods=["POST"])**
**def login():**: POST method to receive login email and password and then direct to the dashboard. server side error handling for incomplete fields and wrong password input

**@app.route("/register", methods=["GET","POST"])**
**def register():**GET method to load the register user page. POST method used to receive the input details of new user. server side error handling for 
- incomplete fields
- email as unique login id unavailable

### setup_db.py
**create_db_and_table()**: Creates a database file and a table.
**insert_sample_data()**: Inserts sample data into the table in the database.

### notable mention
**register.html**: from chatgpt.
 - javascript block included to make dynamic check (upon button submit) if the re-entered password matches the password chosen.
