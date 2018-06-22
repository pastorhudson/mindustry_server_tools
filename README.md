## mindustry_server_tools
Tools for administering a headless Mindustry server

### refreshmaps.py
A simple python script that scans the mindustry-maps folder and adds any new png files to the server map list.
What happens when you run it:
* The script scans the folder where the script is run for all png files.
* The script renames all files to lower case.
* The script looks for any files with "oregenoff" in the title and sets them to oreGen off.
* New maps.json is then dumped.

Usage:
Add or remove maps by adding and removing the png files to the mindustry-maps folder.
I have created an "other_maps" folder inside my mindustry-maps folder and I put maps I'm not currently running in there.

Make sure any maps with oregen off have 'oregenoff' somewhere in the filename.

Run the script inside your mindustry-maps folder:

'''
python refreshmaps.py
'''

#### Installing
Copy refreshmaps.py to your server's mindustry-maps folder.
#### Adding And Removing Maps
Simply add or remove .png maps to the mindustry-maps folder and run the script.
python refreshmaps.py

### mindustry_server_discord_bot.py
Mindustry discord bot based on https://github.com/Greenfoot5/GreenBOT and my own added cogs.

### Installing
You need python 3.6 and discord.py rewrite

* Install the discord.py rewrite using:
```
sudo python3.6 -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]
```
* Git clone this repository
* Put your token in token.txt in the mindustry_server_tools folder
* Set your mindustry-maps folder location in /cogs/maps.py
* Run with ''' python3.6 mindustry_discord_bot.py