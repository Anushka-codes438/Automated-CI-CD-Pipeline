from flask import Flask,render_template,request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():

    fullname = request.form["fullname"]
    email = request.form["email"]
    password = request.form["password"]
    confirm_password = request.form["confirm_password"]

    print(f"Full Name: {fullname}")
    print(f"Email: {email}")
    print(f"Password: {password}")
    print(f"Confirm Password: {confirm_password}")

    return """
    <h2>Registration Successful! </h2>
    <a href="/">Go Back</a>
    """


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=5000)