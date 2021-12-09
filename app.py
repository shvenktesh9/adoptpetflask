from flask import Flask,render_template
from forms import SignUpForm , LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'

pets=[{"id":1, "name":"Rocky", "description":"German Shephard"}]
@app.route('/')
def home():
    user={'username':'namrata'}
    return render_template('home.html', user=user, pets=pets)

@app.route('/about')
def about():
    posts=['hello','post1','hello2']
    return render_template('about.html', posts=posts)

@app.route('/login')
def userLogin():
    return render_template('login.html')

@app.route("/signup",methods=["GET","POST"])
def Signup():
    form = SignUpForm()
    return render_template("signup.html", form = form)

@app.route('/details/<int:id>')
def details(id):
    if pets[0]["id"]==id:
        return render_template('details.html', id=id, pet=pets[0])
    



if __name__ == "__main__":
    app.run(debug=True)
