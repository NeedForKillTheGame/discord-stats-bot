import requests


def tdm_find_close_games():
    '''Функция ищет игры ТДМ где была маленькая разница в счете'''
    url = 'https://stats.needforkill.ru/api.php?action=matches&skip=0&take=100'
    response = requests.get(url)
    matches = response.json()
    games_close = {}
    for match in matches:
        if match['gameType'] == 'TDM':
            red_score = int(match["redScore"])
            blue_score = int(match["blueScore"])
            diff_factor = 3
            if abs(red_score - blue_score) <= diff_factor:
                mapname = match['map']
                demo = "https://stats.needforkill.ru/match/" + match['matchID']
                score = str(red_score) + ':' + str(blue_score)
                games_close[mapname] = [demo, score]
    if len(games_close) == 0:
        return 'No games were found, asshole.'

    games_close_overall = []
    for i in sorted(games_close.items(),
                    key=lambda pair: (pair[1][0])):
        games_close_overall.append(i)

    return games_close_overall[::-1]


def ctf_find_close_games():
    '''Функция ищет игры КТФ где была маленькая разница в счете'''
    url = 'https://stats.needforkill.ru/api.php?action=matches&skip=0&take=300'
    response = requests.get(url)
    matches = response.json()
    games_close = {}
    for match in matches:
        if match['gameType'] == 'CTF':
            red_score = int(match["redScore"])
            blue_score = int(match["blueScore"])
            humiliation_factor = 1
            if abs(red_score - blue_score) <= humiliation_factor:
                mapname = match['map']
                demo = "https://stats.needforkill.ru/match/" + match['matchID']
                score = str(red_score) + ':' + str(blue_score)
                games_close[mapname] = [demo, score]
    if len(games_close) == 0:
        return 'No games were found, dumbass.'

    games_close_overall = []
    for i in sorted(games_close.items(),
                    key=lambda pair: (pair[1][0])):
        games_close_overall.append(i)

    return games_close_overall[::-1]
