from flask import Flask, session, request, redirect
app = Flask(__name__)
app.secret_key="secret123"
users = {
    "student":"123",
    "user1":"245",
    "user2":"1243",
    "user3":"999",   
    "user4":"456",  
    "user5":"789"  
}
@app.route("/")
def home():
    if "user" in session:
        return f"Hello {session['user']}! Cart: {session['cart']}<br><a href='/add/Item'>Add Item</a><br><a href='/logout'>Logout</a>"
    return "<form method='POST' action='/login'>User:<input name='u'> Pass:<input name='p' type='password'><button>Login</button></form>"
@app.route("/login", methods=["POST"])
def login():
    username = request.form["u"]
    password = request.form["p"]
    if username in users and users[username] == password:
        session["user"] = username
        session["cart"] = []
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
if __name__ == "__main__":
    app.run(debug=True)
