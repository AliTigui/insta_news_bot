

import asyncio
import discord
from instagrapi import Client # type: ignore
cl = Client()
cl.login("Username", "password")
import sqlite3

con = sqlite3.connect("server.db")
cur = con.cursor()

class MyClient(discord.Client):
    async def write_news(self):
        while True:
            for k in self.guilds:
                g=self.get_guild(k.id)
                res = cur.execute(f"SELECT channel_id FROM servers WHERE server_id = ?",(g.id,))
                try:
                    ch=int(res.fetchone()[0])
                    
                except:
                    continue
                channel = g.get_channel(ch)
                pages = cur.execute("SELECT page FROM pages WHERE server_id = ?",(g.id,))
                pages= list(map(lambda e: e[0],pages))
                for page in pages:
                    await asyncio.sleep(60) 
                    
                    try:
                        user_id = cl.user_id_from_username(page)
                        code = cl.user_medias(user_id, 1)[0].code.strip()
                    except:
                        continue
                    codes = cur.execute("SELECT post_code FROM posted WHERE server_id = ?",(g.id,))
                    codes = list(map(lambda e: e[0],codes))
                
                    if not( code in codes):
                        await channel.send("https://www.instagram.com/p/"+code)
                        cur.execute("INSERT INTO posted (server_id,post_code) VALUES(?,?)",(g.id,code))
                        con.commit()
            
 
    async def on_ready(self):

        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        await self.write_news()
    async def on_message(self, message):
        self.channel=int(message.channel.id)
        self.server=int(message.guild.id)
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!news') and message.author.guild_permissions.ban_members:
            res = cur.execute("SELECT * FROM servers WHERE server_id  = ?",(self.server,))
            if res.fetchone() is None:
                cur.execute("INSERT INTO servers VALUES (?,?)",(self.server,self.channel))
                con.commit()
            else :
                cur.execute("UPDATE servers SET channel_id = ? WHERE server_id   = ?",(self.channel,self.server))
                con.commit()
            
        if message.content.startswith('!add_insg') and message.author.guild_permissions.ban_members:
            in_page = message.content.split()[1].strip()
            res = cur.execute("SELECT * FROM pages WHERE server_id = ? AND page= ?",(self.server,in_page))
            if res.fetchone() is None:
                print( in_page)
                cur.execute("INSERT INTO pages (server_id,page) VALUES (?,?)",(self.server,in_page))
                con.commit()
            


            

            

                

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

client.run('your token')
