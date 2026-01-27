import requests
import asyncio
import os
import logging

async def parse_json(json_data):

    try:
        username = json_data['username']
        uid = json_data['uid']
        rank = json_data['rank']
        level = json_data['level']
        total_wins = json_data['total_wins']
        total_games = json_data['total_games']
        win_rate = json_data['win_rate']
        logging.info("JSON parsed successfully.")

        return {
            "username": username,
            "uid": uid,
            "rank": rank,
            "level": level,
            "total_wins": total_wins,
            "total_games": total_games,
            "win_rate": win_rate
        }
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to retrieve data: {e}")
        return