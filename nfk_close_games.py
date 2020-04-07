import find_games_score


def tdm_find_close_games():
    '''Функция ищет игры ТДМ где была маленькая разница в счете'''
    return find_games_score.find_games_score('TDM', 'close')


def ctf_find_close_games():
    '''Функция ищет игры КТФ где была маленькая разница в счете'''
    return find_games_score.find_games_score('CTF', 'close')
