from telethon.sync import TelegramClient

# Your API ID and hash
api_id = '22217088'
api_hash = 'f331334dbd9057c54803742a5d248e9f'

# User ID of the recipient
user_id = 'edi_me'

# Message to send
message = 'Hello, this is a test message from my Telegram bot!'

# Create a TelegramClient instance
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    # Connect to Telegram
    await client.start()

    try:
        # Send the message to the recipient
        await client.send_message(user_id, message)
        print("Message sent successfully!")
    except Exception as e:
        print(f"Error sending message: {e}")
    finally:
        # Disconnect from Telegram
        await client.disconnect()

# Run the main function
with client:
    client.loop.run_until_complete(main())
