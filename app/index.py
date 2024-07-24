from flask import render_template, request

from rps_game import RPSGame


# TODO auth
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        data = {
            "name_1": request.form.get("name_1"),
            "name_2": request.form.get("name_2"),
            "move_1": request.form.get("move_1"),
            "move_2": request.form.get("move_2"),
        }
        game = RPSGame(data)
        results = game.play()
        return render_template("index.html", results=results)
