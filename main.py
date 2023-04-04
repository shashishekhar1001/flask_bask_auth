from flask import Flask, render_template, url_for, request, session, redirect, flash, Response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///E:/Flask_Basic_Auth/SRC/database.db'
app.config['SECRET_KEY'] = '$ztKK&8Urww*e5@I2e$Dd^d212e12eG1'

db = SQLAlchemy(app)

login_manager = LoginManager ()
login_manager.init_app (app)

# Customize User Model Here 
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100))

    def __repr__(self):
        return '<User %r>' % self.username


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    if 'email' in session:
        return f'Logged in as {session["email"]}'
    return 'You are not logged in'

# @app.route('/login')
# def login():
#     return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists!')
            return redirect(url_for('signup'))
        if password == confirm_password:
            new_user = User(email=email, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        else:
            flash('Passwords do not match!')
            return redirect(url_for('signup'))
    else:
        if 'email' in session:
            return 'You are already logged in!'
        return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        next_url = request.form.get("next")
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return render_template('login.html')
        login_user(user)
        session['email'] = request.form['email']
        if next_url:
            return redirect(next_url)
        return redirect(url_for('index'))
    else:
        if 'email' in session:
            return 'You are already logged in!'
        return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    session.pop('email', None)
    logout_user()
    return 'You are now logged out!'

@app.route('/home')
@login_required
def home():
    return 'The current user Email is ' + current_user.email

@app.errorhandler(401)
def custom_401(error):
    return redirect(url_for("login", next=request.url))
    # return Response('<Why access is denied string goes here...>', 401, {'WWW-Authenticate':'Basic realm="Login Required"'})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)