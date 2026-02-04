import requests
import asyncio
import os
import logging

# Enable logging
logging.basicConfig(level=logging.DEBUG)  # You can change to INFO or WARNING later

#Local Variables
base_url_v1 = "https://marvelrivalsapi.com/api/v1"
base_url_v2 = "https://marvelrivalsapi.com/api/v2"

def get_api_key():
    # Find the secrets.txt file one level above this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    secrets_path = os.path.join(parent_dir, 'secrets/secrets.txt')
    api_key = ""

    # read your api key from a file
    with open(secrets_path, "r") as f:
        lines = f.readlines()
        api_key = lines[5].strip()

    logging.info(f"local api_key retrieved successfully.")

    return api_key

async def search_player(username):

    try:
        api_key = get_api_key()
        headers = {"x-api-key": api_key}
        response = requests.get(f"{base_url_v1}/find-player/{username}", headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        logging.info("Data retrieved successfully.")

        #Uncomment to test
        # print(data)

        return data
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to retrieve data: {e}")
        return
    
async def player_stats(username):

    search_player_data = await search_player(username)
    uid = search_player_data['uid']

    logging.info(f"uid {uid} retrieved based on username {username}.")

    try:
        api_key = get_api_key()
        headers = {"x-api-key": api_key}

        all_season_data = {}

        for season in range(1, 7):  # seasons 1 through 6

            logging.info(f"Requesting data for season {season}.")

            response = requests.get(f"{base_url_v1}/player/{uid}?season={season}", headers=headers)
            response.raise_for_status()
            data = response.json()

            logging.info(f"Data for season {season} retrieved successfully.")
            
            all_season_data[season] = data  # or append to a list if you prefer


        #Uncomment to test
        print(all_season_data)

        logging.info(f"Data for all seasons retrieved successfully.")

        return all_season_data
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to retrieve data: {e}")
        return

# run this example
asyncio.run(search_player("TouchingUrSups"))
# asyncio.run(player_stats("ApexDabi"))