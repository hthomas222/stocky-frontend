from flask import Flask, render_template, request
import yfinance as yf


app = Flask(__name__)


@app.route('/')
def main():
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


# if __name__ == '__main__':
#      app.run(port=8080, debug=True)
