import discord
import asyncio


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        if message.content.startswith('!sayi'):
            msg = await message.channel.send('10')
            await asyncio.sleep(3.0)
            await msg.edit(content='40')

    async def on_message_edit(self, before, after):
        msg = f'**{before.author}** edited their message:\n{before.content} -> {after.content}'
        await before.channel.send(msg)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTE5NjE0Njk1NTk3MDE3MTAwMg.GVbzCv.rfouz8B9TBBd2StuJgQsLYTguuEZfse_hroAEA')