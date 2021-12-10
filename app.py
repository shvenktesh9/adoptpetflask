from flask import Flask,render_template
from forms import SignUpForm , LoginForm
from flask import session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///paws.db'
db = SQLAlchemy(app)

"""Model for Pets."""
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    age = db.Column(db.String)
    bio = db.Column(db.String)
    posted_by =  db.Column(db.String, db.ForeignKey('user.id'))


"""Model for Users."""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    pets = db.relationship('Pet', backref = 'user')

db.create_all() 

pets=[{"id":1, "name":"Rocky", "description":"German Shephard"}]
users = [
            {"id": 1, "full_name": "Pet", "email": "t@pets.co", "password": "password"},
        ]
@app.route('/')
def home():
    user={'username':'namrata'}
    return render_template('home.html', user=user, pets=pets)

@app.route('/about')
def about():
    posts=['hello','post1','hello2']
    return render_template('about.html', posts=posts)

@app.route('/login',methods=["GET","POST"])
def Login():
    form = LoginForm()
    if form.validate_on_submit():
        for u_email,u_password in users.items():
            if u_email==form.email.data and u_password==form.password.data:
                return render_template("login.html",message="success")
        return render_template("login.html",message="unsuccessful")
    elif form.errors:
        print(form.errors.items())
    return render_template('login.html', form = form)

@app.route("/signup",methods=["GET","POST"])
def Signup():
    form = SignUpForm()
    if form.validate_on_submit():
        new_user = {"id": len(users)+1, "full_name": form.full_name.data, "email": form.email.data, "password": form.password.data}
        users.append(new_user)
        return render_template("signup.html", message = "Successfully signed up")
    return render_template("signup.html", form = form)

@app.route('/details/<int:id>')
def details(id):
    if pets[0]["id"]==id:
        return render_template('details.html', id=id, pet=pets[0])
    



if __name__ == "__main__":
    app.run(debug=True)
