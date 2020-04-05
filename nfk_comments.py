import requests


def find_comments():
    '''Функция ищет игры где 3 и больше комментариев'''
    url = 'https://stats.needforkill.ru/api.php?action=matches&skip=0&take=500'
    response = requests.get(url)
    matches = response.json()
    games_comments = {}
    for match in matches:
        if int(match['comments']) >= 2:
                mapname = match['map']
                game = "https://stats.needforkill.ru/match/" + match['matchID']
                games_comments[mapname] = game
    if len(games_comments) == 0:
        return 'No games were found. Stop asking and go fuck yourself.'
    games_comments_overall = []
    for i in sorted(games_comments.items(),
                    key=lambda pair: (pair[1])):
        games_comments_overall.append(i)

    return games_comments_overall[::-1]
