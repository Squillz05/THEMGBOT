import tweepy
import os
from dotenv import load_dotenv
import discord

load_dotenv("keys.env")

T_API_KEY = os.getenv("T_API_KEY")
T_API_SECRET_KEY = os.getenv("T_API_SECRET_KEY")
T_ACCESS_TOKEN = os.getenv("T_ACCESS_TOKEN")
T_ACCESS_TOKEN_SECRET = os.getenv("T_ACCESS_TOKEN_SECRET")
T_BEARER_TOKEN = os.getenv("T_BEARER_TOKEN")
T_CLIENT_ID = os.getenv("T_CLIENT_ID")
T_CLIENT_SECRET = os.getenv("T_CLIENT_SECRET")
D_TOKEN = os.getenv("D_TOKEN")

client = tweepy.Client(
    bearer_token=T_BEARER_TOKEN,
    consumer_key=T_API_KEY,
    consumer_secret=T_API_SECRET_KEY,
    access_token=T_ACCESS_TOKEN,
    access_token_secret=T_ACCESS_TOKEN_SECRET,
)



def verifyauthtwitter():
    try:
        auth_out = client.get_me()
        if auth_out.data:
            print("Twitter:Authentication OK")
        else:
            print("Twitter:Authentication failed")
    except Exception as e:
        print(f"Twitter:Error during authentication: {e}")

def t_post(input_text):
    try:
        post_out = client.create_tweet(text=input_text)
        print(f"Twitter:Posted! Tweet ID: {post_out.data['id']}")
    except Exception as e:
        print(f"Twitter:Error during posting: {e}")

def d_post(input_text, channel_id):
    try:
        intents = discord.Intents.default()
        client = discord.Client(intents=intents)

        @client.event
        async def on_ready():
            channel = client.get_channel(channel_id)
            if channel:
                await channel.send(input_text)
                print(f"Discord: Message sent to channel")
            await client.close()

        client.run(D_TOKEN)
    except Exception as e:
        print(f"Discord: Error during posting: {e}")


def twitter_run(input_text):
    verifyauthtwitter()

    t_post(input_text)

def discord_run(input_text, channel_id):
    d_post(input_text, channel_id)


def main():
    d_answer = input("Post To Discord (Y or N): ").strip().upper()
    t_answer = input("Post To Twitter (Y or N): ").strip().upper()
    discord_flag = d_answer == 'Y'
    twitter_flag = t_answer == 'Y'

    if discord_flag or twitter_flag:

        input_text = input("Text To Tweet/Discord: ")

        link_answer = input("Add A link? (Y or N): ").strip().upper()
        if link_answer == 'Y':
            link_text = input("Enter the link: ").strip()
            input_text = f"{input_text} {link_text}"

        if discord_flag:
            # channel_id = int(input("Enter Discord Channel ID: ").strip())
            channel_id = 1316984386217840662
            discord_run(input_text, channel_id)
        if twitter_flag:
            twitter_run(input_text)


    print("__________SUCESSFULLY___RAN___MG_____BOT__________")
    return


if __name__ == '__main__':
   main()