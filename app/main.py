from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to Docker Lunch and Learn! Happy Birthday to me"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
