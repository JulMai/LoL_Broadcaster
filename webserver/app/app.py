from flask import Flask
from flask import render_template, send_file, redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/champ_select')
def champ_select():
    return "Champselect_Pictures"

@app.route('/champ_select/team1')
def team1():
    return "Team1"

@app.route('/champ_select/team1/player1')
def team1_player1():
    return redirect('https://ddragon.leagueoflegends.com/cdn/img/champion/splash/MonkeyKing_0.jpg')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')