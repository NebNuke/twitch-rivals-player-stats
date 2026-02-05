# ws_listener.py
import asyncio
from hashlib import new
from twitchAPI.eventsub.websocket import EventSubWebsocket
from twitchAPI.twitch import Twitch
from twitchAPI.type import AuthScope
from twitchAPI.helper import first
import os
import channel_point_events as ch_pt_evts
import cheer_events as chr_evts
import auth
import twitch_classes


async def main():
    # Authenticate using your auth module
    twitch_auth = await auth.twitch_auth()

    # Get the Twitch user ID from the username
    user = await first(twitch_auth.get_users(logins='ApexDabi'))

    print("Authenticated Twitch user:", user)
    user_id = user.id
    print("User ID:", user_id)

    # Start the WebSocket listener
    eventsub = EventSubWebsocket(twitch_auth)
    eventsub.start()

    print(twitch_auth.get_user_auth_scope())

    # Subscribe to the channel.point event
    # await eventsub.listen_channel_points_automatic_reward_redemption_add_v2(user_id, ch_pt_evts.handle_channel_point_event)
    await eventsub.listen_channel_points_automatic_reward_redemption_add(
        user_id,
        ch_pt_evts.handle_channel_point_event
    )

    # Subscribe to the channel.cheer event
    # eventsub.listen_channel_cheer(user_id, chr_evts.handle_cheer_event)

    print("WebSocket listener is running...")

    # Keep the script running
    while True:
        await asyncio.sleep(1)

# Run the listener
asyncio.run(main())
