# 274597252880662528
# discore
# batishkin gosteva9a 259124796971941890
# discord.gg/bratishkin

import discord
import random
import string
import asyncio

client = discord.Client()


def random_phrase(length):
    return ''.join(random.choice(string.ascii_uppercase) for i in range(length))

inEmail = input("email: ")
inPassword = input("password: ")
inChannel = input("Channel id: ")


@client.event
async def on_ready():
    print("Find out how much messages you need to send to reach wanted lvl on mee6calc.xyz")
    msg_to_send = int(input("How how much messages you need to send: "))
    while msg_to_send > 0:
        msg_to_send -= 1
        rnd_out = random_phrase(5) + "-" + random_phrase(5) + "-" + random_phrase(5) + "-" + random_phrase(5)
        await client.send_message(client.get_channel(inChannel), rnd_out)
        await asyncio.sleep(50)
    return

client.run(inEmail, inPassword)
