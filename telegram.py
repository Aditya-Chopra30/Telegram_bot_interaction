from telethon.sync import TelegramClient

api_id = '*******' # use your api id 
api_hash = '******************************' # use your api hash 

# User ID of the recipient
user_id = '****'

Message to send
message = 'hello, this is a test message from my Telegram bot!'

# creating a TelegramClient instance
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    # Connect to Telegram
    await client.start()

    try:
        # Sending the message to the recipient
        await client.send_message(user_id, message)
        print("Message sent successfully!")
    except Exception as e:
        print(f"Error sending message: {e}")
    finally:
        # Disconnect from Telegram
        await client.disconnect()

#  main function
with client:
    client.loop.run_until_complete(main())
