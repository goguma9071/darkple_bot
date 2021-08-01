import discord
import asyncio
import random
client = discord.Client()

token = "당신의 봇 토큰을 쓰세요"

@client.event
async def on_ready():
    print(client.user.name)
    print("사용법: !dp [명령어]")
    game = discord.Game("!dp 도와줘")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content == "!dp 서버장은":
        await message.channel.send("god")
    if message.content == "!dp 오팬무":
        await message.channel.send("주황")
    if message.content == "!dp 뒤져 이시키야":
        await message.channel.send("너나뒤져 ㅗ")
    if message.content == "!dp 스태프는":
        await message.channel.send("친구 최대한 많이 끌고오면 스태프줌 근데 부를때에도 응답없을시 0명간주")
    if message.content == "!dp 도와줘":
        await message.channel.send("사용법: !dp [명령어] 명령어: 서버장은,오팬무,뒤져 이시키야,스테프는,도와줘")




client.run(token)

