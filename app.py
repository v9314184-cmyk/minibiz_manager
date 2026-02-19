from flask import Flask, render_template, request, redirect

app = Flask(__name__)

income_total = 0
expense_total = 0

@app.route("/", methods=["GET", "POST"])
def home():
    global income_total, expense_total

    if request.method == "POST":
        amount = float(request.form["amount"])
        category = request.form["category"]

        if category == "income":
            income_total += amount
        else:
            expense_total += amount

        return redirect("/")

        profit = income_total - expense_total
        return render_template(
            "index.html",
            income=income_total,
            expense=expense_total,
            profit=profit
        )

if __name__ == "__main__":
    app.run()
