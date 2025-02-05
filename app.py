from flask import Flask, render_template, request, redirect, url_for
import yfinance as yf


app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/auth', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('test'))
    return render_template("auth.html", error=error)


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
