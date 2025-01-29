from flask import Flask, render_template, url_for

import h2hcalc
from h2hcalc import read_h2h_dict, CURRENT_SEASON, players


app = Flask(__name__)

def get_ordered_list(h2h_dict, p1):
    h2h_list = []
    if p1 in h2h_dict:
        for p2 in h2h_dict[p1]:
            h2h_list.append(p2)
        h2h_list.sort(key=lambda x: players.index(x))
    return h2h_list


@app.route("/")
def home():
    h2hcalc.load_players()
    h2h_dict = read_h2h_dict()
    return render_template("index.html", title="Home Page", current_season=CURRENT_SEASON, players=players[:10], h2h_dict=h2h_dict, get_ordered_list=get_ordered_list)

@app.route("/top10")
def top10():
    h2hcalc.load_players()
    h2h_dict = read_h2h_dict()
    return render_template("head-to-head.html", title="Top 10 Head-to-Head Table", current_season=CURRENT_SEASON, players=players[:10], h2h_dict=h2h_dict, get_ordered_list=get_ordered_list)

@app.route("/top50")
def top50():
    h2hcalc.load_players()
    h2h_dict = read_h2h_dict()
    return render_template("head-to-head.html", title="Top 50 Head-to-Head Table", current_season=CURRENT_SEASON, players=players[:50], h2h_dict=h2h_dict, get_ordered_list=get_ordered_list)

@app.route("/major-winners")
def major_winners():
    h2hcalc.load_players()
    h2h_dict = read_h2h_dict()
    major_winners = ['Zain', 'Cody Schwab', 'Mang0', 'Hungrybox', 'aMSa', 'Jmook', 'moky', 'Leffen', 'Wizzrobe', 'Plup']
    return render_template("head-to-head.html", title="Major Winner Head-to-Head Table", current_season=CURRENT_SEASON, players=major_winners, h2h_dict=h2h_dict, get_ordered_list=get_ordered_list)

