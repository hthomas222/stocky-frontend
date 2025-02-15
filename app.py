from flask import Flask, render_template, request, redirect, url_for
import yfinance as yf
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash 


app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/auth', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        un = request.form['username']
        pw = request.form['password']
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for i in rows:
            if un == i[1]: 
                if pw == i[2]:
                    return redirect(url_for('test'))
                else:
                    error = 'Invalid Credentials. Please try again.'
            else: 
                error = 'Invalid Credentials. Please try again.'
        conn.close()
        return render_template("auth.html", error=error)
    return render_template("auth.html", error=error)


@app.route('/create-user', methods=['GET', 'POST'])
def create_user():
    return render_template("register.html")


@app.route('/create-user/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        un = request.form['user']
        pw = request.form['pw']
        if len(pw) >= 12:
            con = sqlite3.connect("users.db")
            cur = con.cursor()
            cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (un,pw))
            con.commit()
            con.close()
            return render_template("auth.html", error=error)
        else: 
            error="Password must be longer than 12!"
            return render_template("register.html", error=error)
    return render_template("register.html", error=error)

@app.route('/home')
def test():
    return render_template("index.html")


@app.route("/stock-results/", methods=["POST"])
def packages():
    if request.method == 'POST':
        stock = request.form["stock"]
        i = stock.upper()
        ticker = yf.Ticker(i).info
        s = ticker["symbol"]
        op = ticker['open']
        dl = ticker['dayLow']
        dh = ticker['dayHigh']
        pc = ticker['previousClose']
        return render_template("index.html", s=s, op=op, dl=dl, dh=dh, pc=pc)
    return render_template("index.html")


@app.route('/logout')
def logout():
    return redirect("/")



if __name__ == '__main__':
     app.run(port=8080, debug=True)


