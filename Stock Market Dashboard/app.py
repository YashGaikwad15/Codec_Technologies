from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd

app = Flask(__name__)

# Default settings
DEFAULT_TICKER = "AAPL"
HISTORY_PERIOD = "1mo"
CHART_COLOR = "#2ecc71"

@app.route("/", methods=["GET", "POST"])
def index():
    data = None
    ticker = DEFAULT_TICKER

    if request.method == "POST":
        ticker_input = request.form.get("ticker")
        if ticker_input:
            ticker = ticker_input.upper()

    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=HISTORY_PERIOD)

        if hist.empty:
            data = []  # No data found
        else:
            hist.reset_index(inplace=True)
            hist['Date'] = hist['Date'].dt.strftime('%Y-%m-%d')  # Convert Timestamp to string
            data = hist[['Date', 'Close']].to_dict(orient='records')
    except Exception as e:
        print("Error fetching data:", e)
        data = []

    return render_template("index.html", data=data, ticker=ticker, chart_color=CHART_COLOR)

if __name__ == "__main__":
    app.run(debug=True)
