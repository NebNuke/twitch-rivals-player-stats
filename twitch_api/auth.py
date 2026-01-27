from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.type import AuthScope
from twitchAPI.helper import first
import asyncio
import os
import logging

# Enable TwitchAPI logging
logging.basicConfig(level=logging.DEBUG)  # You can change to INFO or WARNING later
logger = logging.getLogger('twitchAPI')
logger.setLevel(logging.DEBUG)

#Local Variables
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)

async def twitch_auth():

    # Find the secrets.txt file one level above this script
    secrets_path = os.path.join(parent_dir, 'secrets.txt')
    twitch = None
    app_id = ""
    app_secret = "" 

    # read your app credentials from a file
    with open(secrets_path, "r") as f:
        lines = f.readlines()
        app_id = lines[1].strip()
        app_secret = lines[3].strip()

    # initialize the twitch instance, this will by default also create a app authentication for you
    try:
        # Create Twitch app instance
        twitch = Twitch(app_id, app_secret)

        # Define required scopes
        target_scope = [AuthScope.USER_READ_EMAIL]

        # Run interactive OAuth flow (opens browser)
        auth = UserAuthenticator(twitch, target_scope)
        token, refresh_token = await auth.authenticate()

        # Apply and await user auth to twitch instance
        await twitch.set_user_authentication(token, target_scope, refresh_token)

        logger.info("Twitch initialized with user authentication.")

        return twitch
        
    except Exception as e:
        logger.error(f"Failed to authenticate Twitch: {e}")
        return
    
"""
# Test the authentication function
    user = await first(twitch.get_users(logins='NebNuke'))
    # print the ID of your user or do whatever else you want with it
    print(user.id)

# run this example
asyncio.run(twitch_auth())
"""