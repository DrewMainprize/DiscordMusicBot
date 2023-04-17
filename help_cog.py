import discord
from discord.ext import commands

class help_cog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

		self.help_message = """
```
General Commands:
/help - display all commands
/play <keyword> - find song on Youtube and play
/pause - pause the current song
/resume - resume the current song
/queue - display the current queue
/skip - skip the current song
/clear - stop music and clear queue
/leave - disconnect the bot
```
"""

		self.text_channel_text = []

	@commands.Cog.listener()
	async def on_ready(self):
		for guild in self.bot.guilds:
			for channel in guild.text_channels:
				self.text_channel_text.append(channel)

		await self.send_to_all(self.help_message)

	async def send_to_all(self, msg):
		for text_channel in self.text_channel_text:
			await text_channel.send(msg)

	@commands.command(name="help", help="display all commands")
	async def help(self, ctx):
		await ctx.send(self.help_message)


