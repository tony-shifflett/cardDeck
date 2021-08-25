from flask import Flask

app = Flask(__name__)

@app.route("/")
def test ():
    return "Basic Functionality Running"

if __name__ == '__main__':
    app.run(debug=True)