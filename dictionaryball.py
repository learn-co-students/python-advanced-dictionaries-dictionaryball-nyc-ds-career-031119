game_dictionary = {
    "home":{
        "team_name":"Brooklyn Nets", 
        "colors":["Black", "White"], 
        "players":{
            "Alan Anderson":{
                "number":0,
                "shoe":16,
                "points":22,
                "rebounds":12,
                "assists":12,
                "steals":3,
                "blocks":1,
                "slam_dunks":1},
            "Reggie Evans":{
                "number":30,
                "shoe":14,
                "points":12,
                "rebounds":12,
                "assists":12,
                "steals":12,
                "blocks":12,
                "slam_dunks":7},
            "Brook Lopez":{
                "number":11,
                "shoe":17,
                "points":17,
                "rebounds":19,
                "assists":10,
                "steals":3,
                "blocks":1,
                "slam_dunks":15},
            "Mason Plumlee":{
                "number":1,
                "shoe":19,
                "points":26,
                "rebounds":12,
                "assists":6,
                "steals":3,
                "blocks":8,
                "slam_dunks":5},
            "Jason Terry":{
                "number":31,
                "shoe":15,
                "points":19,
                "rebounds":2,
                "assists":2,
                "steals":4,
                "blocks":11,
                "slam_dunks":1}}},
    "away":{
        "team_name":"Charlotte Hornets", 
        "colors":["Turquoise", "Purple"], 
        "players":{
            "Jeff Adrien":{
                "number":4,
                "shoe":18,
                "points":10,
                "rebounds":1,
                "assists":1,
                "steals":2,
                "blocks":7,
                "slam_dunks":2},
            "Bismak Biyombo":{
                "number":0,
                "shoe":16,
                "points":12,
                "rebounds":4,
                "assists":7,
                "steals":7,
                "blocks":15,
                "slam_dunks":10},
            "DeSagna Diop":{
                "number":2,
                "shoe":14,
                "points":24,
                "rebounds":12,
                "assists":12,
                "steals":4,
                "blocks":5,
                "slam_dunks":5},
            "Ben Gordon":{
                "number":8,
                "shoe":15,
                "points":33,
                "rebounds":3,
                "assists":2,
                "steals":1,
                "blocks":1,
                "slam_dunks":0},
            "Brendan Haywood":{
                "number":33,
                "shoe":15,
                "points":6,
                "rebounds":12,
                "assists":12,
                "steals":22,
                "blocks":5,
                "slam_dunks":12}}}}

def game_dict():
    return game_dictionary


def num_points_scored(name):
    for team in game_dict():
        if name in game_dict()[team]['players']:
            return game_dict()[team]['players'][name]['points']


def shoe_size(name):
    for team in game_dict():
        if name in game_dict()[team]['players']:
            return game_dict()[team]['players'][name]['shoe']
        
        
def team_colors(team_name):
    for team in game_dict():
        if team_name in game_dict()[team]['team_name']:
            return game_dict()[team]['colors']

        
def team_names():
    team_names = []
    for team in game_dict():
        team_names.append(game_dict()[team]['team_name'])
    return team_names


def player_numbers(team_name):
    numbers = []
    for team in game_dict():
        if team_name in game_dict()[team]['team_name']:
            for player in game_dict()[team]['players']:
                numbers.append(game_dict()[team]['players'][player]['number'])
    return sorted(numbers)


def player_stats(name):
    for team in game_dict():
        if name in game_dict()[team]['players']:
            return game_dict()[team]['players'][name]

        
def big_shoe_rebounds():
    shoe_size = []
    for team in game_dict():
        for name in game_dict()[team]['players']:
            shoe_size.append(game_dict()[team]['players'][name]['shoe'])
    highest = max(shoe_size)
    
    for team in game_dict():
        for name in game_dict()[team]['players']:
            if highest ==  game_dict()[team]['players'][name]['shoe']:
                return game_dict()[team]['players'][name]['rebounds']
          
        
def winning_team():
    points = []
    for team in game_dict():
        home = []
        for name in game_dict()[team]['players']:
            home.append(game_dict()[team]['players'][name]['points'])
            points.append(sum(home))
    max_points = max(points)
    for team in game_dict():
        home = []
        for name in game_dict()[team]['players']:
            home.append(game_dict()[team]['players'][name]['points'])
            total = sum(home)
            if max_points == total:
                return (game_dict()[team]['team_name'])
    
    
def most_points_scored():
    points = {}
    for team in game_dict():
        for name in game_dict()[team]['players']:
            points[name] = game_dict()[team]['players'][name]['points']
    return [k for k, v in points.items() if v == max(points.values())]


def player_with_longest_name():
    players = {}
    for team in game_dict():
        for name in game_dict()[team]['players']:
            players[name] = len(name)
    return [k for k, v in players.items() if v == max(players.values())]


def long_name_steals_a_ton():
    p = {}
    for team in game_dict():
        for name in game_dict()[team]['players']:
            p[name] = game_dict()[team]['players'][name]['rebounds']
    
    if [k for k, v in p.items() if v == max(p.values())] == player_with_longest_name():
        return True
    else:
        return False
