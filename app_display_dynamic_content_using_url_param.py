from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home() :
    return "Welcome, please add '/greet?name=YourName' to the URL to see the dynamic content"

@app.route("/greet")
def greet() :
    name = request.args.get('name', 'Guest')
    return f"Hello, {name}! Welcome to this app which has been made by using Flask. I, Rohit Kumar Gupta, wish you luck and have a good day"

if __name__ == "__main__" :
    app.run(port=5007, debug=True)