from flask import Flask, render_template, request, redirect

app = Flask(__name__)

records = []

@app.route("/")
def home():
    income = sum(r["amount"] for r in records if r["type"] == "income")
    expense = sum(r["amount"] for r in records if r["type"] == "expense")
    profit = income - expense

    return render_template(
        "index.html",
        records=records,
        income=income,
        expense=expense,
        profit=profit
    )

@app.route("/add", methods=["POST"])
def add():
    description = request.form["description"]
    amount = float(request.form["amount"])
    record_type = request.form["type"]

    records.append({
        "description": description,
        "amount": amount,
        "type": record_type
    })

    return redirect("/")
    if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
