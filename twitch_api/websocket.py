# ws_listener.py
import asyncio
from auth import TwitchAuth
from twitchAPI.eventsub.websocket import EventSubWebsocket
from twitchAPI.type import AuthScope
import os


async def main():
    # Authenticate using your auth module
    auth = await TwitchAuth()
    twitch = await auth.authenticate()

    # # Get the Twitch user ID from the username
    # user_info = await twitch.get_users(logins=[CHANNEL_NAME])
    # user_id = user_info['data'][0]['id']

    # # Start the WebSocket listener
    # eventsub = EventSubWebsocket(twitch)
    # eventsub.start()

    # # Subscribe to the channel.cheer event
    # await eventsub.listen_channel_cheer(user_id, handle_cheer_event)

    # print("WebSocket listener is running...")

    # # Keep the script running
    # while True:
    #     await asyncio.sleep(1)

# Run the listener
asyncio.run(main())
