from telethon.sync import TelegramClient
from telethon import events

# Your API ID and hash
api_id = '*******'
api_hash = '*****'

# User ID of the recipient
user_id = '*****'

# Message to send
message = 'i am back'

# Create a TelegramClient instance
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    # Connect to Telegram
    await client.start()

    try:
        # Send the message to the recipient
        await client.send_message(user_id, message)
        print("Message sent successfully!")
        
        # Define an event handler to listen for incoming messages
        @client.on(events.NewMessage(chats=user_id))
        async def handler(event):
            print("Message received!")
            print(f"Message content: {event.message.message}")
            print(f"From user ID: {event.sender_id}")

        # Run the event loop
        await client.run_until_disconnected()

    except Exception as e:
        print(f"Error sending/receiving messages: {e}")
    finally:
        # Disconnect from Telegram
        await client.disconnect()

# Run the main function
with client:
    client.loop.run_until_complete(main())
