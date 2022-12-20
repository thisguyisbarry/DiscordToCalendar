This is a bot that automates the process of converting a discord channel with messages in the format of

Event:
 
Location:
 
Date:
 
Time:
 
Decisions to be made:
 
Links (if appropriate):


It will then create, or add to, a google calendar list so that people can subscribe and automatically have any events created in their calendars without having to keep up to date with a discord channel.


Above the minimum viable product (TODO):

Bot should moderate the event channel in discord.
 
By having a helper command to set up events, and by deleting peoples irrelevant messages in the top level channel (outside thread).
Ensure that the thread for each event in discord is added.

Remove events that have gone past the date within the discord. 

After an event is created using a commend, the persons command message should be deleted for clean up (or a seperate event creation channel if that works better),

People should be told off for posting outisde of a thread with anything other than an appropriate command. (Keep this to DMs, no need to spam the channel with nonsense, people and bots)

Dependancies:

Python 3.10.1

Discord.py for Python Discord Library:

py -3 -m pip install -U discord.py

For working with enviromental variables for secrets:

pip3 install python-dotenv
