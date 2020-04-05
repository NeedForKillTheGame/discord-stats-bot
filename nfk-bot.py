import discord
from discord.ext import commands
import random
import nfk_stats as ns
import nfk_punishment as np
import nfk_close_games as ncg
import nfk_comments as nc
import nfk_long_games as nlg


client = commands.Bot(command_prefix="!")


@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Ошибка, как и весь род человеческий.')


@client.event
async def on_ready():
    print('I am ready to put my shaft up your ass! Please bow down.')
    await client.change_presence(status=discord.Status.idle,
                                 activity=discord.Game('NFK Stats'))


@client.event
async def on_message(message):
    if message.author.bot:
        return
    elif message.content.startswith('Hello'):
            await message.channel.send(
                'Лапшу из местной столовой тебе в хайло!')
    elif message.content.startswith('Hi'):
            await message.channel.send('Хуяй блять, англичашек развелось!')
    elif message.content.startswith('Привет'):
            await message.channel.send('Привет, мясо.')
    elif message.content.endswith('привет'):
            await message.channel.send('Приветик, кусок костей.')
    elif message.content.startswith('Здоров'):
            await message.channel.send('И тебе не хворать, человекообразный.')
    elif message.content.startswith('Здрав'):
        await message.channel.send('Касперского мне в жопу, кого я вижу!')
    await client.process_commands(message)


@client.command()
async def ping(ctx, help='Пингует бота'):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question, help='Спросите бота что угодно'):
    responses = [
                 'Yes', 'Ты дурашка, рассолу перепил с утра?', 'IDDQD',
                 'No', 'Дураков на Руси лет на сто припасено', 'IDKFA',
                 'Are you medieval?', 'Советую прямо сейчас и приступить.',
                 'Твоему тимеру не повезло больше чем твоим врагам',
                 'Иди на дм0 тактику поищи.', 'Даешь машинган 50!', 'Нфкака',
                 'А ты попадаешь рейлом в дырочку?', 'Хороший вопрос...',
                 'Я в таких вопросах разбираться не желаю.', 'Согласен, уныло',
                 'А ты сядь попой на плиту и проверь!', 'Ты тимкиллер года!',
                 ]
    await ctx.send(f'Вопрос: {question}\nМыслебот: {random.choice(responses)}')


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=(amount + 1))


@client.command()
async def maps_tdm(ctx, help='Recent TDM games sorted by maps'):
    maps = ns.tdm_maps()
    for map in maps:
        await ctx.send(f'{map[0]} games played: {map[1]}')


@client.command()
async def maps_ctf(ctx, help='Recent CTF games sorted by maps'):
    maps = ns.ctf_maps()
    for map in maps:
        await ctx.send(f'{map[0]} games played: {map[1]}')


@client.command()
async def maps_duel(ctx, help='Recent 1v1 games sorted by maps'):
    maps = ns.duel_maps()
    for map in maps:
        await ctx.send(f'{map[0]} games played: {map[1]}')


@client.command()
async def tdm_pain(ctx, help='Searches for TDM games with high score difference'):
    games_hum = np.tdm_find_hum_games()
    try:
        for game in games_hum:
            await ctx.send(f'Map {game[0]}, {game[1][0]}, {game[1][1]}')
    except:
        await ctx.send(f'{games_hum}')


@client.command()
async def ctf_pain(ctx, help='Searches for CTF games with high score difference'):
    games_hum = np.ctf_find_hum_games()
    try:
        for game in games_hum:
            await ctx.send(f'Map {game[0]}, {game[1][0]}, {game[1][1]}')
    except:
        await ctx.send(f'{games_hum}')


@client.command()
async def tdm_close(ctx, help='Searches for close TDM games'):
    games_close = ncg.tdm_find_close_games()
    try:
        for game in games_close:
            await ctx.send(f'Map {game[0]}, {game[1][0]}, {game[1][1]}')
    except:
        await ctx.send(f'{games_close}')


@client.command()
async def ctf_close(ctx, help='Searches for close CTF games'):
    games_close = ncg.ctf_find_close_games()
    try:
        for game in games_close:
            await ctx.send(f'Map {game[0]}, {game[1][0]}, {game[1][1]}')
    except:
        await ctx.send(f'{games_close}')


@client.command()
async def comments(ctx, help='Searches games with comments'):
    games_comments = nc.find_comments()
    try:
        for game in games_comments:
            await ctx.send(f'Map {game[0]}, {game[1]}')
    except:
        await ctx.send(f'{games_comments}')


@client.command()
async def tdm_long(ctx, help='Finds TDM games with overtime'):
    games_long = nlg.find_long_tdm()
    try:
        for game in games_long:
            await ctx.send(f'Map {game[0]}, {game[1][0]}, {game[1][1]}')
    except:
        await ctx.send(f'{games_long}')


@client.command()
async def ctf_long(ctx, help='Finds long CTF games'):
    games_long = nlg.find_long_ctf()
    try:
        for game in games_long:
            await ctx.send(f'Map {game[0]}, {game[1][0]}, {game[1][1]}')
    except:
        await ctx.send(f'{games_long}')


client.run('Njk1MjY0ODE2NzcxNzYwMTkw.XoYMDw.Tzz1cG2UPl5YfXEiPuY9V5DhuGs')
