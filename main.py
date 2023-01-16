import discord
import handle


client = discord.Client(intents=discord.Intents.all())

async def send_message(message, user_message):
    try:
        response = handle.handle_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    username = str(message.author)
    user__message = str(message.content)
    channel = str(message.channel)

    print(f"{username} said '{user__message}' ({channel})")
    await send_message(message, user__message)

@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} edit a message.\n'
        f'before: ( {before.content} )\n'
        f'After: ( {after.content} )\n'
        f'Therefor {before.author} fucked up.'
    )


TOKEN = 'MTA2MzQ0Mjc1MDA0Njk5ODYyOQ.G6JyZF.ZQ61Q6EenJckYcoY4lUm2dsqR1Y2KlL_BARSSw'

client.run(TOKEN)