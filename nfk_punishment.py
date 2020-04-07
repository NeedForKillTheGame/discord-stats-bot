import find_games_score


def tdm_find_hum_games():
    '''Функция ищет игры ТДМ где была большая разница в счете'''
    return find_games_score.find_games_score('TDM', 'big')


def ctf_find_hum_games():
    '''Функция ищет игры КТФ где была большая разница в счете'''
    return find_games_score.find_games_score('CTF', 'big')
