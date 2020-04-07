import requests


def find_games_score(gametype, diff_criteria):
    '''Ищет игры по разнице в счете и отдает их как отсортированный словарь'''
    url = 'https://stats.needforkill.ru/api.php?action=matches&skip=0&take=100'
    response = requests.get(url)
    matches = response.json()
    games_close = {}
    for match in matches:
        if match['gameType'] == gametype:
            red_score = int(match['redScore'])
            blue_score = int(match['blueScore'])
            if gametype == 'TDM' and diff_criteria == 'close':
                diff_factor = 3
            elif gametype == 'CTF' and diff_criteria == 'close':
                diff_factor = 1
            elif gametype == 'TDM' and diff_criteria == 'big':
                diff_factor = 30
            elif gametype == 'CTF' and diff_criteria == 'big':
                diff_factor = 5

            if diff_criteria == 'close':
                if abs(red_score - blue_score) <= diff_factor:
                    game = ("https://stats.needforkill.ru/match/" +
                            match['matchID'])
                    mapname = match['map']
                    score = str(red_score) + ':' + str(blue_score)
                    games_close[game] = [mapname, score]
            elif diff_criteria == 'big':
                if abs(red_score - blue_score) >= diff_factor:
                    game = ("https://stats.needforkill.ru/match/" +
                            match['matchID'])
                    mapname = match['map']
                    score = str(red_score) + ':' + str(blue_score)
                    games_close[game] = [mapname, score]

    if len(games_close) == 0:
        return 'No games were found, asshole.'

    games_close_overall = []
    for i in sorted(games_close.items(),
                    key=lambda pair: (pair[0])):
        games_close_overall.append(i)

    return games_close_overall[::-1]
