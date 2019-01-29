import discord
import youtube_dl
from discord.ext import commands

TOKEN = "" #Add your bot token here
client = commands.Bot(command_prefix = '!')

players = {}

@client.event
async def on_ready():
    print("Bot is online.")

#!connect command
@client.command(pass_context=True)
async def connect(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

#!disconnect command
@client.command(pass_context=True)
async def disconnect(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

#play command
@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

#pause command
@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()

#resume commands
@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

#stop command
@client.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()


client.run(TOKEN)
