import discord

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('/merhaba'):
        await message.channel.send("Merhaba")
    elif message.content.startswith('/bye'):
        await message.channel.send("Olamaz sen gidemezsin!")
    else:
        await message.channel.send(message.content)

client.run("MTE5NjE0Njk1NTk3MDE3MTAwMg.GVbzCv.rfouz8B9TBBd2StuJgQsLYTguuEZfse_hroAEA")
