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

def cheer_event_bucky():
    try:
        # Play BUCKY!! sound
        playsound(os.path.join(assets_dir, 'BUCKY!!.m4a'))
        
    except Exception as e:
        logging.error(f"Failed to play BUCKY!! sound: {e}")
        return

def cheer_event_theburntpeanut_hooray():
    try:
        # Play THEBURNTPeanut Hooray sound
        playsound(os.path.join(assets_dir, 'THEBURNTPeanut_Hooray.mp3'))
        
    except Exception as e:
        logging.error(f"Failed to play THEBURNTPeanut Hooray sound: {e}")
        return

def cheer_event_theburntpeanut_lets_ride():
    try:
        # Play THEBURNTPeanut Lets Ride sound
        playsound(os.path.join(assets_dir, 'THEBURNTPeanut_Lets_Ride.mp3'))
        
    except Exception as e:
        logging.error(f"Failed to play THEBURNTPeanut Lets Ride sound: {e}")
        return

def cheer_event_theburntpeanut_mhmmm_mhmmm():
    try:
        # Play THEBURNTPeanut MHMMM MHMMM sound
        playsound(os.path.join(assets_dir, 'THEBURNTPeanut_MHMMM_MHMMM.mp3'))
        
    except Exception as e:
        logging.error(f"Failed to play THEBURNTPeanut MHMMM MHMMM sound: {e}")
        return

def cheer_event_ahh_horse_shit():
    try:
        # Play THEBURNTPeanut AHH HORSE SHIT sound
        playsound(os.path.join(assets_dir, 'AHH_HORSE_SHIT.mp3'))
        
    except Exception as e:
        logging.error(f"Failed to play AHH HORSE SHIT sound: {e}")
        return

def cheer_event_giant_horse_conch():
    try:
        # Play THEBURNTPeanut Giant Horse Conch sound
        playsound(os.path.join(assets_dir, 'GIANT_HORSE_CONCH.mp3'))
        
    except Exception as e:
        logging.error(f"Failed to play GIANT HORSE CONCH sound: {e}")
        return

def cheer_event_horse_race_music():
    try:
        # Play THEBURNTPeanut Horse Race Music sound
        playsound(os.path.join(assets_dir, 'HORSE_RACE_MUSIC.mp3'))
        
    except Exception as e:
        logging.error(f"Failed to play HORSE RACE MUSIC sound: {e}")
        return

def cheer_event_the_horse_is_here():
    try:
        # Play THEBURNTPeanut The Horse Is Here sound
        playsound(os.path.join(assets_dir, 'PETER_THE_HORSE_IS_HERE.mp3'))
        
    except Exception as e:
        logging.error(f"Failed to play THE HORSE IS HERE sound: {e}")
        return

async def handle_cheer_event(event):
    bits = event['event']['bits']
    user = event['event']['user_name']
    type = event['event']['type']
    logging.info(f"{user} cheered {bits} bits!")

    if type != "cheer":
        logging.warning("Event type is not 'cheer'. Exiting handler.")
        return
    else:
        logging.info("Event type is 'cheer'. Proceeding with sound triggers.")

        # Special sound triggers for specific bit amounts
        if bits == 1000:
            cheer_event_bucky()
        elif bits == 1001:
            cheer_event_theburntpeanut_hooray()
        elif bits == 1002:
            cheer_event_theburntpeanut_lets_ride()
        elif bits == 1003:
            cheer_event_theburntpeanut_mhmmm_mhmmm()
        elif bits == 1004:
            cheer_event_ahh_horse_shit()
        elif bits == 1005:
            cheer_event_giant_horse_conch()
        elif bits == 1006:
            cheer_event_horse_race_music()
        elif bits == 1007:
            cheer_event_the_horse_is_here()
        else:
            # Replace with whatever sound trigger you like
            logging.info(f"No special sound for this bit amount: {bits}")



# # Testing loop
# async def test_loop():
#     for bits in range(1000, 1008):  # 1000 to 1007 inclusive
#         test_event = {
#             'event': {
#                 'bits': bits,
#                 'user_name': 'NebNuke'
#             }
#         }
#         await handle_cheer_event(test_event)
#         await asyncio.sleep(0.5)  # Optional delay between events

# # Run the test loop
# asyncio.run(test_loop())