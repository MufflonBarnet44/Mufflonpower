from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello this is mainPage  <h1>HALLOJSA<H1>"
if __name__ == "__main__":
    app.run()


print("skriptet körs faktsikt")