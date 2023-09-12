import logging
import asyncio
from aiogram import Bot, Dispatcher
from datetime import datetime
import RPi.GPIO as GPIO

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create a bot instance
bot = Bot(token='token')

# Create a dispatcher
dp = Dispatcher(bot)

# set maximum alarm messages
max_messages = 3
count_messages = 0

async def send_message_to_group(group_id, message):
    # Function to send a message to the specified group
    await bot.send_message(chat_id=group_id, text=message)

async def send_message_on_condition():
    while True:      
        # GPIO numbering according to GPIO numbering
        GPIO.setmode(GPIO.BCM)

        # Declare GPIO as input
        GPIO.setup(17, GPIO.IN)

        if GPIO.input(17) == 1:
            # reset message count
            count_messages = 0

            # Add group id here
            group_id = -123

            # Get current date and time on each iteration
            current_time = datetime.now().time()

            # Check if it's Sunday and time is between 11:14 and 11:16
            if (datetime.now().weekday() == 6 and
                datetime.strptime('11:14', '%H:%M').time() <= current_time <= datetime.strptime('11:16', '%H:%M').time()):
                message = r"FFW Kreisprobealarm"  # Message for Sunday between 11:14 and 11:16 am
            else:
                message = r"🚨 FFW EINSATZ! 🚨"  # Default message for other times

            while count_messages < max_messages:
                await send_message_to_group(group_id, message)
                count_messages =+ 1

        # Clean up GPIO resources
        GPIO.cleanup()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_message_on_condition())
