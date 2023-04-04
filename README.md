# flask_login_example
Basic Barebone Flask authentication Web App using Flask Login !

<br />

# Root Page to check if user is logged in or not!
http://localhost:5000
[![Auth-1.png](https://i.postimg.cc/rmv8fH5S/Auth-1.png)](https://postimg.cc/34F5RnSR)

<br />

<br />

# Access Restricted Home page :
http://localhost:5000/home
[![Auth-2.png](https://i.postimg.cc/d3wprgQQ/Auth-2.png)](https://postimg.cc/ftq8h201)

<br />

<br />

# Access Restricted Home page after login :
http://localhost:5000/home
[![Auth-3.png](https://i.postimg.cc/4dJQ5Gc0/Auth-3.png)](https://postimg.cc/FfBSr2Db)

<br />

<br />

# Logout User :
http://localhost:5000/logout
[![Auth-4.png](https://i.postimg.cc/QCSFbLzD/Auth-4.png)](https://postimg.cc/D4JfvNFp)

<br />


<br />

# Signup Page :
http://localhost:5000/signup
[![Auth-5.png](https://i.postimg.cc/jdz4wDtF/Auth-5.png)](https://postimg.cc/XpYCt7Zf)

<br />


# 👉 Set Up for Windows
Install modules via VENV (windows)
```bash
$ virtualenv env
$ .\env\Scripts\activate
$ pip3 install -r requirements.txt
```
<br />

# 👉 Set Up for Unix, MacOS
Install modules via VENV
```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

<br />

# How to run :
```bash
$python main.py
```
<br />
At this point, the app runs at http://127.0.0.1:5000/.
<br />


# ✨ Code-base structure:
<br />

```bash
<PROJECT ROOT>:
|   .gitignore
# |   database.db                      # You need to configure and create
|   main.py                            # App Entry
|   README.md
|   requirements.txt
|   
+---templates
|       login.html
|       signup.html
```
<br />

# Note:

Use the correct path to point sqlite db in main.py
```bash
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///E:/Flask_Basic_Auth/SRC/database.db'
``` 
<br />
Create SQlite DB using following commands

```bash
$ python
>>> from main import app, db
>>> app.app_context().push()
>>> db.create_all()
OR
>>> from main import db, app, User
>>> db.create_all(app=create_app())
```
<br />
database.db shall be now created in project root folder