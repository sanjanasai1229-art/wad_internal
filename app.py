from flask import Flask, session, request, redirect
app = Flask(__name__)
app.secret_key="secret123"
@app.route("/")
def home():
    if "user" in session:
        return f"Hello {session['user']}! Cart: {session['cart']}<br><a href='/add/Item'>Add Item</a><br><a href='/logout'>Logout</a>"
    return "<form method='POST' action='/login'>User:<input name='u'> Pass:<input name='p' type='password'><button>Login</button></form>"
@app.route("/login", methods=["POST"])
def login():
    if request.form["u"]=="student" and request.form["p"]=="123":
        session["user"]="student"
        session["cart"]=[]
        return redirect("/")
    return "Invalid!"
@app.route("/add/<item>")
def add(item):
    if "user" in session:
        session["cart"].append(item)
    return redirect("/")
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
if __name__=="__main__":
    app.run(debug=True)
