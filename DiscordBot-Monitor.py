import discord
import urllib.request
import bs4 as bs
from bs4 import BeautifulSoup

# Create the Soup for BeautifulSoup
url_target = 'https://www.endclothing.com/eu/latest-products/latest-sneakers'       
sauce_1  = urllib.request.urlopen(url_target).read()
soup_1 = bs.BeautifulSoup(sauce_1, 'lxml')


# Let's initialize the DiscordBot
client = discord.Client()

# Function that read Discord message
@client.event
async def on_message (message):
    global item
    item = str(message.content) # Var for your message on Discord (that will contain the shoe ID)
    
    Boolean_for_while = True
    my_href = ""
    items = ""
    my_id = ""
    
    while Boolean_for_while:
        for items in (soup_1.find_all('a', class_ = 'sc-1koxpgo-0 bTJixI sc-5sgtnq-2 gHSLMJ', id=item )):     # Search the ID of the shoe in the HTML
            my_data = soup_1.find_all('a', id= item, class_ = 'sc-1koxpgo-0 bTJixI sc-5sgtnq-2 gHSLMJ')
            for x in my_data:
                my_href = x.get("href")
                my_id = x.get('id')
        
           
        if item in my_id or item == my_id:

            await message.channel.send('I FIND YOUR ITEM HERE: https://www.endclothing.com'+my_href) # If it find the item the DiscordBot will send you a message
            print('I FIND YOUR ITEM HERE: ','https://www.endclothing.com'+my_href)
            
            Boolean_for_while = False
            exit()
  
        if item not in my_id:
            await message.channel.send("I haven't found your item yet, but I keep looking...")       # If it doesn't find the item it will keep looking
            keep_looking()
            
            Boolean_for_while = False
            exit()


# Function that continues to search for the item until it finds it (same code of the previous fuction)
def keep_looking():

    Boolean_for_while = True
    my_href = ""
    items = ""
    my_id = ""

    while Boolean_for_while:
        for prods in (soup_1.find_all('a', class_ = "sc-1koxpgo-0 bTJixI sc-5sgtnq-2 gHSLMJ", id=item )):
            my_data = soup_1.find_all("a", id= item, class_ = 'sc-1koxpgo-0 bTJixI sc-5sgtnq-2 gHSLMJ')
            for x in my_data:
                my_href = x.get("href")
                my_id = x.get('id')
        
           
        if item in my_id or item == my_id:
            @client.event
            async def on_message (message):
                await message.channel.send('I FIND YOUR ITEM HERE: https://www.endclothing.com'+my_href)
                exit()
            
                Boolean_for_while = False
                pass
        else:
          print('I KEEP LOOKING...')
    client.run('YOUR_DISCORD_TOKEN_BOT(IF YOU DON'T KNOW WHAT I AM TALKING ABOUT, LOOK AT THIS:https://www.youtube.com/watch?v=xdg39s4HSJQ)')

 

        



        





            
client.run('YOUR_DISCORD_TOKEN_BOT(IF YOU DON'T KNOW WHAT I AM TALKING ABOUT, LOOK AT THIS:https://www.youtube.com/watch?v=xdg39s4HSJQ)')
