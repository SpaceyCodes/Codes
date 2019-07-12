import discord
import time
import random
timenow = str(time.asctime())
list = {1: 'None', 2: 'None',3: 'None',4: 'None'}
timing = {}
timingmin = {5: 5, 10: 10, 15: 15, 30: 30, 60: 60, 90: 90, 120: 120}
timingsec = {10: 10, 9: 9, 8: 8, 7: 7, 6: 6, 5: 5, 4: 4, 3: 3, 2: 2, 1: 1}
rpsltn = {'rock': 1, 'paper':2, 'scissor':3}
rpsntl = {1: 'rock', 2: 'paper', 3: 'scissor'}
rpslose = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
rpswin = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
rpsbotscore = {1: 0}
rpsplayerscore = {1: 0}
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        game = discord.Game("|Bot CK| ?help")
        await client.change_presence(status=discord.Status.online, activity=game)


    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        if message.content.startswith('?hello'):
            embed = discord.Embed(
                description = 'Hello sir.',
                colour = discord.Colour.green()
                )
            await message.channel.send(embed=embed)
        elif message.content.startswith('?q'):
            embed = discord.Embed(
                title = '这个世界上没有天才，只有不努力的笨蛋。',
                colour = discord.Colour.green()
                )
            await message.channel.send(embed=embed)
        elif message.content.startswith('?help'):
            embed = discord.Embed(
                title = "< Lists of Commands >",
                colour = discord.Colour.green()
                )
            embed.add_field(name = 'Say hi:', value='- ?hello',inline=False)
            embed.add_field(name = 'Quote:', value='- ?q',inline=False)
            embed.add_field(name = 'Check if Bot CK is alive:', value='- ?bot',inline=False)
            embed.add_field(name = 'Tells current time:', value='- ?time',inline=False)
            embed.add_field(name = 'My website:', value='- ?web',inline=False)
            embed.add_field(name = 'Notes:', value='- ?notes <type out note>',inline=False)
            embed.add_field(name = 'Delete notes:', value='- ?delnotes <type out note no.>',inline=False)
            embed.add_field(name = 'Clear all notes:', value='- ?clearnotes',inline=False)
            embed.add_field(name = 'Set a Countdown:', value='- ?cd <type out in minutes>',inline=False)
            embed.add_field(name = 'Play Rock,Paper,Scissor:', value='- ?rps <rock/paper/scissor>',inline=False)
            embed.add_field(name = 'Clear score:', value='- ?clearrps',inline=False)
            await message.channel.send(embed=embed)

        elif message.content.startswith('?bot'):
            embed = discord.Embed(
                description = 'Bot is up and running!!!',
                colour = discord.Colour.green()
                )
            await message.channel.send(embed=embed)
        elif message.content.startswith('?time'):
            embed = discord.Embed(
                title = "Time is:",
                description = timenow,
                colour = discord.Colour.green()
                )
            await message.channel.send(embed=embed)
        elif message.content.startswith("?web"):
            embed = discord.Embed(
                title = "My website:",
                description = "gay.com",
                colour = discord.Colour.green()
                )
            await message.channel.send(embed=embed)
        elif message.content.startswith("?notes"):
            content = message.content
            if content == '?notes':
                embed = discord.Embed(
                title = ":notepad_spiral:Notes",
                colour = discord.Colour.green()
                )
                embed.add_field(name= '------', value=list.get(1),inline=False)
                embed.add_field(name= '------', value=list.get(2),inline=False)
                embed.add_field(name= '------', value=list.get(3),inline=False)
                embed.add_field(name= '------', value=list.get(4),inline=False)
                await message.channel.send(embed=embed)
            elif message.content.startswith("?notes "):
                content = content.replace('?notes ', '')
                if list.get(1) == 'None':
                    list[1]= content
                    embed = discord.Embed(
                        title = ":notepad_spiral:Notes",
                        colour = discord.Colour.green()
                        )
                    embed.add_field(name= '------', value=list.get(1),inline=False)
                    embed.add_field(name= '------', value=list.get(2),inline=False)
                    embed.add_field(name= '------', value=list.get(3),inline=False)
                    embed.add_field(name= '------', value=list.get(4),inline=False)
                    await message.channel.send(embed=embed)
                elif list.get(2) == 'None':
                    list[2]= content
                    embed = discord.Embed(
                        title = ":notepad_spiral:Notes",
                        colour = discord.Colour.green()
                        )
                    embed.add_field(name= '------', value=list.get(1),inline=False)
                    embed.add_field(name= '------', value=list.get(2),inline=False)
                    embed.add_field(name= '------', value=list.get(3),inline=False)
                    embed.add_field(name= '------', value=list.get(4),inline=False)
                    await message.channel.send(embed=embed)
                elif list.get(3) == 'None':
                    list[3]= content
                    embed = discord.Embed(
                        title = ":notepad_spiral:Notes",
                        colour = discord.Colour.green()
                        )
                    embed.add_field(name= '------', value=list.get(1),inline=False)
                    embed.add_field(name= '------', value=list.get(2),inline=False)
                    embed.add_field(name= '------', value=list.get(3),inline=False)
                    embed.add_field(name= '------', value=list.get(4),inline=False)
                    await message.channel.send(embed=embed)
                elif list.get(4) == 'None':
                    list[4]= content
                    embed = discord.Embed(
                        title = ":notepad_spiral:Notes",
                        colour = discord.Colour.green()
                        )
                    embed.add_field(name= '------', value=list.get(1),inline=False)
                    embed.add_field(name= '------', value=list.get(2),inline=False)
                    embed.add_field(name= '------', value=list.get(3),inline=False)
                    embed.add_field(name= '------', value=list.get(4),inline=False)
                    await message.channel.send(embed=embed)

                elif len(list) == 4:
                    embed = discord.Embed(
                        description = 'Notes is full.',
                        colour = discord.Colour.green()
                        )
                    await message.channel.send(embed=embed)

                    return

        elif message.content.startswith("?delnotes "):
            content = message.content
            content = int(content.replace('?delnotes ', ''))
            list.update({content: 'None'})
            embed = discord.Embed(
                title = ":notepad_spiral:Notes",
                colour = discord.Colour.green()
                )
            embed.add_field(name= '------', value=list.get(1),inline=False)
            embed.add_field(name= '------', value=list.get(2),inline=False)
            embed.add_field(name= '------', value=list.get(3),inline=False)
            embed.add_field(name= '------', value=list.get(4),inline=False)
            await message.channel.send(embed=embed)
        elif message.content.startswith("?clearnotes"):
            list.update({1: 'None'})
            list.update({2: 'None'})
            list.update({3: 'None'})
            list.update({4: 'None'})
            embed = discord.Embed(
                title = ":notepad_spiral:Notes",
                colour = discord.Colour.green()
                )
            embed.add_field(name= '------', value=list.get(1),inline=False)
            embed.add_field(name= '------', value=list.get(2),inline=False)
            embed.add_field(name= '------', value=list.get(3),inline=False)
            embed.add_field(name= '------', value=list.get(4),inline=False)
            await message.channel.send(embed=embed)
        elif message.content.startswith("?cd "):
            content = message.content
            content = content.replace('?cd ', '')
            content = int(content)
            timing[1]=0
            while isinstance(content, int) and timing.get(1) == 0:
                if content > 1:
                    embed = discord.Embed(
                        title = 'Time left: %smin' %content,
                        colour = discord.Colour.green()
                        )
                    await message.channel.send(embed=embed)
                while content != 1:
                    content -= 1
                    time.sleep(60)
                    if content == timingmin.get(content):
                        embed = discord.Embed(
                            title = 'Time left: %smin' %content,
                            colour = discord.Colour.green()
                            )
                        await message.channel.send(embed=embed)
                if content == 1:
                    contentsec = content * 60
                    embed = discord.Embed(
                        title = 'Time left: %smin' %content,
                        colour = discord.Colour.green()
                        )
                    await message.channel.send(embed=embed)
                while contentsec != 0: 
                    contentsec -= 1
                    time.sleep(1)
                    if contentsec == timingsec.get(contentsec):
                        embed = discord.Embed(
                          title = 'Time left: %ssec' %contentsec,
                           colour = discord.Colour.green()
                            )
                        await message.channel.send(embed=embed)
                embed = discord.Embed(
                    title = 'Time is up.',
                    colour = discord.Colour.green()
                    )
                await message.channel.send(embed=embed)

        elif message.content.startswith("?rps "):
            content = message.content
            content = content.replace('?rps ', '')
            if content == 'scissors' or content == 'paper' or content == 'rock':
                botrps = random.randint(1,3)
                if botrps == 3:
                    embed = discord.Embed(
                        title = 'Player|{}-{}|Comp'.format(rpsplayerscore.get(1), rpsbotscore.get(1)),
                        description = '{} draws with {}'.format(content, content),
                        colour = discord.Colour.green()
                        )
                    await message.channel.send(embed=embed)
                elif botrps == 2:
                    rpsbotscore[1]= rpsbotscore.get(1)+1
                    embed = discord.Embed(
                        title = 'Player|{}-{}|Comp'.format(rpsplayerscore.get(1), rpsbotscore.get(1)),
                        description = '{} loses to {}'.format(content, rpslose.get(content)),
                        colour = discord.Colour.green()
                        )
                    await message.channel.send(embed=embed)
                elif botrps == 1:
                    rpsplayerscore[1]= rpsplayerscore.get(1)+1
                    embed = discord.Embed(
                        title = 'Player|{}-{}|Comp'.format(rpsplayerscore.get(1), rpsbotscore.get(1)),
                        description = '{} wins against {}'.format(content, rpswin.get(content)),
                        colour = discord.Colour.green()
                        )
                    await message.channel.send(embed=embed)
        elif message.content.startswith("?clearrps"):
            rpsbotscore[1]=0
            rpsplayerscore[1]=0
            embed = discord.Embed(
                title = 'Score cleared.',
                colour = discord.Colour.green()
                )
            await message.channel.send(embed=embed)






client = MyClient()
client.run('NTk1OTIwMDE4NDc5MjUxNDc2.XRyCRA.OHbq_akgBkP59lUP3DmrUvRFIe4') #DO NOT SHARE THIS TOKEN!!!!!!!!!!!!

