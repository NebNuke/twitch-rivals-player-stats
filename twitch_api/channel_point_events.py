from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.type import AuthScope
from twitchAPI.helper import first
from playsound3 import playsound
import asyncio
import os
import logging

#Local Variables
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
assets_dir = os.path.join(parent_dir, 'assets\\audio\\')

def channel_point_event_bucky():
    try:
        # Play BUCKY!! sound
        playsound(os.path.join(assets_dir, 'BUCKY!!.m4a'))
        
    except Exception as e:
        logging.error(f"Failed to play BUCKY!! sound: {e}")
        return


async def handle_channel_point_event(event):
    cost = event['event']['cost']
    user = event['event']['user_name']

    print(f"{user} used {cost} channel points!")

    # Special sound triggers for specific bit amounts
    if cost == 2000:
        channel_point_event_bucky()
    elif cost == 1000:
        channel_point_event_bucky()
    else:
        # Replace with whatever sound trigger you like
        print("No special sound for this channel point cost: ", cost)



# # Testing loop
# async def test_loop():
#     for cost in range(2000, 2001):  # 2000 to 2000 inclusive
#         test_event = {
#             'event': {
#                 'cost': cost,
#                 'user_name': 'NebNuke'
#                 ,'title': 'Posture Check!'
#             }
#         }
#         await handle_channel_point_event(test_event)
#         await asyncio.sleep(0.5)  # Optional delay between events

# # Run the test loop
# asyncio.run(test_loop())