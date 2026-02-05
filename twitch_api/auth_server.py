# auth_server.py 
# A simple Flask server to handle Twitch OAuth2 authentication flow
# ONLY EXECUTE THIS SCRIPT TO GET A FRIEND TOKEN AND SAVE IT TO friend_token.json
# DO NOT IMPORT THIS MODULE IN OTHER SCRIPTS
from flask import Flask, request, redirect
import requests
import json
import webbrowser
import os

#Local Variables
REDIRECT_URI = 'http://localhost:5000/callback'
SCOPES = ['channel:read:redemptions', 'bits:read']
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
secrets_path = os.path.join(parent_dir, 'secrets/secrets.txt')

# read your app credentials from a file
def get_secrets():
    with open(secrets_path, "r") as f:
        lines = f.readlines()
        app_id = lines[1].strip()
        app_secret = lines[3].strip()
    return app_id, app_secret

AUTH_URL = (
    f"https://id.twitch.tv/oauth2/authorize"
    f"?client_id={get_secrets()[0]}"
    f"&redirect_uri={REDIRECT_URI}"
    f"&response_type=code"
    f"&scope={' '.join(SCOPES)}"
)

app = Flask(__name__)

@app.route('/')
def start():
    return redirect(AUTH_URL)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_url = 'https://id.twitch.tv/oauth2/token'
    data = {
        'client_id': get_secrets()[0],
        'client_secret': get_secrets()[1],
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': REDIRECT_URI
    }

    res = requests.post(token_url, data=data)
    token_data = res.json()

    # Save token to file
    with open('friend_token.json', 'w') as f:
        json.dump(token_data, f, indent=2)

    return "Authorization complete! You can close this window."

if __name__ == '__main__':
    print(f"Opening browser to authorize Twitch account...")
    webbrowser.open('http://localhost:5000')
    app.run(port=5000)
