from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        return render_template("thanks.html", name=name)

    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=True)
