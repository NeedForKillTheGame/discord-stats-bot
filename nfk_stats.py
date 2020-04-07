import requests


def tdm_maps():
    '''Функция показывает количество игр, сыгранных на ТДМ картах'''
    url = 'https://stats.needforkill.ru/api.php?action=matches&skip=0&take=300'
    response = requests.get(url)
    matches = response.json()
    maps_tdm = []
    for match in matches:
        if match['gameType'] == 'TDM':
            maps_tdm.append(match['map'])
    if len(maps_tdm) == 0:
        return 'No games were found, asshole.'
    maps_played_TDM = {}
    for map in maps_tdm:
        if map not in maps_played_TDM:
            maps_played_TDM[map] = 1
        else:
            maps_played_TDM[map] += 1

    maps_TDM_overall = []
    for i in sorted(maps_played_TDM.items(),
                    key=lambda pair: (pair[1])):
        maps_TDM_overall.append(i)

    return maps_TDM_overall[::-1]


def ctf_maps():
    '''Функция показывает количество игр, сыгранных на КТФ картах'''
    url = 'https://stats.needforkill.ru/api.php?action=matches&skip=0&take=200'
    response = requests.get(url)
    matches = response.json()
    maps_ctf = []
    for match in matches:
        if match['gameType'] == 'CTF':
            maps_ctf.append(match['map'])
    if len(maps_ctf) == 0:
        return 'No games were found, asshole.'
    maps_played_CTF = {}
    for map in maps_ctf:
        if map not in maps_played_CTF:
            maps_played_CTF[map] = 1
        else:
            maps_played_CTF[map] += 1

    maps_CTF_overall = []
    for i in sorted(maps_played_CTF.items(),
                    key=lambda pair: (pair[1])):
        maps_CTF_overall.append(i)

    return maps_CTF_overall[::-1]


def duel_maps():
    '''Функция показывает количество игр, сыгранных на 1в1 картах'''
    url = 'https://stats.needforkill.ru/api.php?action=matches&skip=0&take=100'
    response = requests.get(url)
    matches = response.json()
    maps_duel = []
    for match in matches:
        if match['gameType'] == 'DUEL':
            maps_duel.append(match['map'])
    if len(maps_duel) == 0:
        return 'No games were found, asshole.'
    maps_played_DUEL = {}
    for map in maps_duel:
        if map not in maps_played_DUEL:
            maps_played_DUEL[map] = 1
        else:
            maps_played_DUEL[map] += 1

    maps_DUEL_overall = []
    for i in sorted(maps_played_DUEL.items(),
                    key=lambda pair: (pair[1])):
        maps_DUEL_overall.append(i)

    return maps_DUEL_overall[::-1]
