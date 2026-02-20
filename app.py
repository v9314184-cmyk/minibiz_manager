from flask import Flask, render_template, request

app = Flask(__name__)

transactions = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        amount = float(request.form["amount"])
        category = request.form["category"]
        transactions.append((amount, category))

    income = sum(t[0] for t in transactions if t[1] == "income")
    expense = sum(t[0] for t in transactions if t[1] == "expense")
    profit = income - expense

    return render_template("index.html", income=income, expense=expense, profit=profit)

if __name__ == "__main__":
    app.run(debug=True)
