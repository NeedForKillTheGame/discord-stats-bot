import requests


def tdm_find_hum_games():
    '''Функция ищет игры ТДМ где была большая разница в счете'''
    url = 'https://stats.needforkill.ru/api.php?action=matches&skip=0&take=100'
    response = requests.get(url)
    matches = response.json()
    games_hum = {}
    for match in matches:
        if match['gameType'] == 'TDM':
            red_score = int(match["redScore"])
            blue_score = int(match["blueScore"])
            humiliation_factor = 30
            if abs(red_score - blue_score) >= humiliation_factor:
                mapname = match['map']
                demo = "https://stats.needforkill.ru/match/" + match['matchID']
                score = str(red_score) + ':' + str(blue_score)
                games_hum[mapname] = [demo, score]
    if len(games_hum) == 0:
        return 'No games were found, asshole.'

    games_hum_overall = []
    for i in sorted(games_hum.items(),
                    key=lambda pair: (pair[1][0])):
        games_hum_overall.append(i)

    return games_hum_overall[::-1]


def ctf_find_hum_games():
    '''Функция ищет игры КТФ где была большая разница в счете'''
    url = 'https://stats.needforkill.ru/api.php?action=matches&skip=0&take=300'
    response = requests.get(url)
    matches = response.json()
    games_hum = {}
    for match in matches:
        if match['gameType'] == 'CTF':
            red_score = int(match["redScore"])
            blue_score = int(match["blueScore"])
            humiliation_factor = 5
            if abs(red_score - blue_score) == humiliation_factor:
                mapname = match['map']
                demo = "https://stats.needforkill.ru/match/" + match['matchID']
                score = str(red_score) + ':' + str(blue_score)
                games_hum[mapname] = [demo, score]
    if len(games_hum) == 0:
        return 'No games were found, dumbass.'
    games_hum_overall = []
    for i in sorted(games_hum.items(),
                    key=lambda pair: (pair[1][0])):
        games_hum_overall.append(i)

    return games_hum_overall[::-1]
