# I import Flask so I can build a web application.
from flask import Flask
# I create my application and give Flask the current module name.
app = Flask(__name__)
# I tell Flask to use this function when someone visits the home page.
@app.route("/")
# I define the function that handles requests to the home page.
def home():
# I send a welcome message back to the visitor.
    return "Welcome to Bella Vista Cafe"
# I tell Flask to use the next function for the about page.
@app.route("/about")
# I define the function that handles requests to the about page.
def about():
# I return a short description of the cafe to the visitor.
    return "Bella Vista Cafe is a friendly neighborhood cafe serving coffee and fresh pastries."
