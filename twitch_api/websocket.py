# ws_listener.py
import asyncio
from hashlib import new
import logging
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

    logging.info(f"Authenticated Twitch user: {user}")
    user_id = user.id

    # Start the WebSocket listener
    eventsub = EventSubWebsocket(twitch_auth)
    eventsub.start()

    # Subscribe to the channel.cheer event
    logging.info("Subscribing to cheer events...")
    await eventsub.listen_channel_cheer(user_id, chr_evts.handle_cheer_event)

    # Subscribe to the channel.point event
    logging.info("Subscribing to channel point redemption events...")
    await eventsub.listen_channel_points_automatic_reward_redemption_add_v2(user_id, ch_pt_evts.handle_channel_point_event)

    # Subscribe to the channel.hype_train.begin event
    logging.info("Subscribing to channel hype train begin events...")
    await eventsub.listen_hype_train_begin(user_id, ch_pt_evts.handle_channel_point_event) # Replace with your own handler if you want different behavior for hype train events

    # Subscribe to the channel.hype_train.progress event
    logging.info("Subscribing to channel hype train progress events...")
    await eventsub.listen_hype_train_progress(user_id, ch_pt_evts.handle_channel_point_event) # Replace with your own handler if you want different behavior for hype train events

    logging.info("WebSocket listener is running...")

    # Keep the script running
    while True:
        await asyncio.sleep(1)

# Run the listener
asyncio.run(main())
