import requests
import json
import os

API_KEY = os.environ.get('LIQUIPEDIA_API_KEY')

CURRENT_SEASON = '2024'
players = []
h2h_dict = {}

def load_players() -> None:
    with open(f"players.txt", "r") as infile:
        for line in infile:
            players.append(line.rstrip())


def write_h2h_dict() -> None:
    with open(f"head_to_head_{CURRENT_SEASON}.json", "w") as outfile:
        json.dump(h2h_dict, outfile)

def read_h2h_dict() -> dict:
    with open(f"head_to_head_{CURRENT_SEASON}.json", "r") as infile:
        return json.load(infile)
    
    
'''def get_tournaments(player):
    url = 'https://api.liquipedia.net/api/v3/match?wiki=smash'
    x = requests.get(url, headers={'Authorization': f'Apikey {API_KEY}', 'Accept': 'application/json'}, params={
                        })'''

def update_head_to_heads(p1, p2, victor):
    if p1 not in players:
        if p1 == victor:
            p1 = p1[0].lower() + p1[1:]
            victor = p1
        else:
            p1 = p1[0].lower() + p1[1:]
    # TODO: Currently assumes each player has only won a single digit number of sets
    if p1 in h2h_dict:
        if p2 in h2h_dict[p1]:
            if victor == p1:
                h2h_dict[p1][p2] = f'{int(h2h_dict[p1][p2][0]) + 1}-{h2h_dict[p1][p2][-1]}'
            else:
                h2h_dict[p1][p2] = f'{h2h_dict[p1][p2][0]}-{int(h2h_dict[p1][p2][-1]) + 1}'
        else:
            if victor == p1:
                h2h_dict[p1][p2] = '1-0'
            else:
                h2h_dict[p1][p2] = '0-1'
    else:
        h2h_dict[p1] = {p2: ''}
        if victor == p1:
            h2h_dict[p1][p2] = '1-0'
        else:
            h2h_dict[p1][p2] = '0-1'

def get_player_data(player):
    url2 = 'https://api.liquipedia.net/api/v1/match'
    player_data = requests.post(url2, data={'apikey': API_KEY, 
                                  'wiki': 'smash', 
                                  'conditions': f'[[date_year::{CURRENT_SEASON}]] AND ([[opponent1::{player}]] OR [[opponent2::{player}]])',
                                  'query': 'opponent1, opponent2, winner, pagename',
                                  'limit': 1000}).json()['result']
    for set in player_data:
        p1 = set['opponent1']
        p2 = set['opponent2']
        victor = set['winner']
        if p2 == player:
            temp_name = p1
            p1 = p2
            p2 = temp_name
        if len(p2) > 1:
            p2_lower = p2[0].lower() + p2[1:]
        if (p2 in players):
            update_head_to_heads(p1, p2, victor)
        elif (p2_lower in players):
            update_head_to_heads(p1, p2_lower, victor)

def main():
    load_players()
    for player in players:
        player = player[0].upper() + player[1:]
        get_player_data(player)
    write_h2h_dict()
    h2h = read_h2h_dict()
    print(json.dumps(h2h, indent=4))

if __name__ == "__main__":
    main()