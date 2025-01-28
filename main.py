import tweepy
import os
from dotenv import load_dotenv

load_dotenv("keys.env")

API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
)

def verifyauth():
    try:
        auth_out = client.get_me()
        if auth_out.data:
            print("Authentication OK")
        else:
            print("Authentication failed")
    except Exception as e:
        print(f"Error during authentication: {e}")

def post(input_text):
    try:
        post_out = client.create_tweet(text=input_text)
        print(f"Posted! Tweet ID: {post_out.data['id']}")
    except Exception as e:
        print(f"Error during posting: {e}")


if __name__ == '__main__':
    verifyauth()
    text = input("Text To Tweet: ")
    post(text)


