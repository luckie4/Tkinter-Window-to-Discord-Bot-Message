from discord.ext import commands
import datetime
import asyncio
    
bot = commands.Bot(command_prefix='!')

async def timer():
    await bot.wait_until_ready()
    channel = bot.get_channel(123456789) # Replace with channel ID that you want to send to

    # Sending the Discord message
    print("Sending Message")
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    text = " " + current_time
    await channel.send(text)
    print("Message Sent")
        
         

    
    await asyncio.sleep(1)
    print("Loop Started")

    # Breaks from the timer function
    exit()

    
# Run the timer function
task = bot.loop.create_task(timer())     

bot.run('') # Discord Bot Token Here


