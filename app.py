from flask import Flask, render_template, request
import game_of_life as gol

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    w, h = "30", "20"
    if request.method == "POST":
        w = request.form.get("width")
        h = request.form.get("height")
    return render_template("index.html", width=w, height=h)

@app.route('/live', methods=["GET", "POST"])
def live():
    if request.method == "POST":
        width = int(request.form.get("width"))
        height = int(request.form.get("height"))
        gol.GameOfLife(width, height)
    g = gol.GameOfLife()
    g.form_new_generation()
    return render_template("live.html", gen=g)

app.debug=True
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)