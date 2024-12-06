from flask import Flask


app = Flask(__name__)


@app.route("/home/<name>")
@app.route("/home")
def home(name="desconhecido"): 
    return f"Olá {name}"


if __name__ == '__main__':
    app.run(debug=True)