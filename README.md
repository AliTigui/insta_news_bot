### Description
this is a discord bot that post news from instagram pages  
it save data of server and channel where is post and post that it posted with the page that post from in sqllte database  

you can check ``schema.sql`` to see the schema of the data base

### install and run 
to install and run the bot you need python installed in your computer 
then run ``pip install -r requirements.txt`` to install all moduls and packages that the bot need  
i used ``instagrapi`` to get data from instagram it need your password and user name so best is to make account for the bot and use it a scripting account  
to run and start the bot change password and user name in ``cl.login("username", "password")`` to your data in bot.py also insert your token
then run ``python bot.py``
### command for the bot
the commands that the bot use are
- ``!news`` to set channel where the bot post it accept only command from mod with ban permission
- ``!add_insg instagram_page`` to add page to the bot data so it fetch new news from it and bost in discord channel
### issuses and updates
with the library [instagrapi](https://github.com/subzeroid/instagrapi) istagram keep detecting the bot so i try add the time gap between each call and still facing same error and somtime it ask my phone number  
so for now i try find better python library or other way to use the instagram api 

feel free to contribute 
