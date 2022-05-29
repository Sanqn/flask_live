
from flask import Flask, render_template
from game_of_life import GameOfLife


app = Flask(__name__)


@app.route("/index")
@app.route("/")
def index():
    GameOfLife(width=20, height=20)
    return render_template("index.html")


@app.route("/live")
def live():
    life = GameOfLife()
    if life.counter > 0:
        life.form_new_generation()
    life.counter += 1
    return render_template("live.html", life=life)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
