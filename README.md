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