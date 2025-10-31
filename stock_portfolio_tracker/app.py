from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130,
    "MSFT": 330
}

# User’s current portfolio (in-memory)
portfolio = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    stock_name = request.form.get("stock_name").upper()
    quantity = int(request.form.get("quantity", 0))

    if stock_name not in stock_prices:
        return render_template("index.html", error=f"❌ Stock '{stock_name}' not found!", portfolio=portfolio)

    total_value = stock_prices[stock_name] * quantity
    portfolio[stock_name] = total_value

    return render_template("index.html", portfolio=portfolio, success=True)

@app.route("/get_portfolio_data")
def get_portfolio_data():
    # Send data as JSON for Chart.js
    return jsonify({
        "labels": list(portfolio.keys()),
        "values": list(portfolio.values())
    })

if __name__ == "__main__":
    app.run(debug=True)
