import logging
import asyncio
from aiogram import Bot, Dispatcher
from datetime import datetime


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create a bot instance
bot = Bot(token='6032574865:AAH50bDupFM-WR3ztYIiTahciwExtMcFtkQ')

# Create a dispatcher
dp = Dispatcher(bot)

# Get current date and time
current_time = datetime.now().time()


async def send_message_to_group(group_id, message):
    # Function to send a message to the specified group
    await bot.send_message(chat_id=group_id, text=message)

async def send_message_on_condition():
    while True:
        # GPIO input condition here
        user_input = input("Enter 'true' to send a message to the group: ")

        if user_input.lower() == "true":
            # Add group id here
            group_id = -1001917264370

            # Check if it's Sunday and time is between 11:14 and 11:16
            if (datetime.now().weekday() == 6 and
                datetime.strptime('11:14', '%H:%M').time() <= current_time <= datetime.strptime('11:16', '%H:%M').time()):
                message = r"FFW Kreisprobealarm"  # Message for Sunday between 11:14 and 11:16 am
            else:
                message = r"🚨 FFW EINSATZ! 🚨"  # Default message for other times

            await send_message_to_group(group_id, message)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_message_on_condition())