import requests


def find_long_tdm():
    '''Функция ищет тдм игры с овертаймом'''
    url = 'https://stats.needforkill.ru/api.php?action=matches&skip=0&take=500'
    response = requests.get(url)
    matches = response.json()
    games_long = {}
    for match in matches:
        if (match['gameType'] == 'TDM') and (int(match['gameTime']) > 900):
            mapname = match['map']
            game = "https://stats.needforkill.ru/match/" + match['matchID']
            gametime_min = str(int(match['gameTime']) // 60) + ':'
            gametime_sec = str(int(match['gameTime']) % 60)
            gametime = gametime_min + gametime_sec
            games_long[mapname] = game, gametime
    if len(games_long) == 0:
        return 'No games were found. Go play some Hedgehogs 2D.'

    games_long_overall = []
    for i in sorted(games_long.items(),
                    key=lambda pair: (pair[1][0])):
        games_long_overall.append(i)

    return games_long_overall[::-1]


def find_long_ctf():
    '''Функция ищет долгие ктф игры'''
    url = 'https://stats.needforkill.ru/api.php?action=matches&skip=0&take=300'
    response = requests.get(url)
    matches = response.json()
    games_long = {}
    for match in matches:
        if (match['gameType'] == 'CTF') and (int(match['gameTime']) >= 1200):
            mapname = match['map']
            game = "https://stats.needforkill.ru/match/" + match['matchID']
            gametime_min = str(int(match['gameTime']) // 60) + ':'
            gametime_sec = str(int(match['gameTime']) % 60)
            gametime = gametime_min + gametime_sec
            games_long[mapname] = game, gametime
    if len(games_long) == 0:
        return 'No games were found. GO PLAY THEM, you inactive piece of shit!'

    games_long_overall = []
    for i in sorted(games_long.items(),
                    key=lambda pair: (pair[1][0])):
        games_long_overall.append(i)

    return games_long_overall[::-1]
