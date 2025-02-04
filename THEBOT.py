import tweepy
import os
from dotenv import load_dotenv
import discord
from TwitchClipDownload import TwitchDownloadMain
from YoutubeClipDownload import YoutubeClipDownloadMain

load_dotenv("keys.env")

T_API_KEY = os.getenv("T_API_KEY")
T_API_SECRET_KEY = os.getenv("T_API_SECRET_KEY")
T_ACCESS_TOKEN = os.getenv("T_ACCESS_TOKEN")
T_ACCESS_TOKEN_SECRET = os.getenv("T_ACCESS_TOKEN_SECRET")
T_BEARER_TOKEN = os.getenv("T_BEARER_TOKEN")
T_CLIENT_ID = os.getenv("T_CLIENT_ID")
T_CLIENT_SECRET = os.getenv("T_CLIENT_SECRET")
D_TOKEN = os.getenv("D_TOKEN")
DISCORD_CHANNEL_ID = os.getenv("DISCORD_CHANNEL_ID")
OUTPUT_FOLDER = os.getenv('OUTPUT_FOLDER')

client = tweepy.Client(
    bearer_token=T_BEARER_TOKEN,
    consumer_key=T_API_KEY,
    consumer_secret=T_API_SECRET_KEY,
    access_token=T_ACCESS_TOKEN,
    access_token_secret=T_ACCESS_TOKEN_SECRET,
)

auth = tweepy.OAuth1UserHandler(
    T_API_KEY,
    T_API_SECRET_KEY,
    T_ACCESS_TOKEN,
    T_ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)

def verifyauthtwitter():
    try:
        user = api.verify_credentials()
        auth_out = client.get_me()
        if auth_out.data and user:
            print("Twitter:Authentication OK")
        else:
            print("Twitter:Authentication failed")
    except Exception as e:
        print(f"Twitter:Error during authentication: {e}")

def t_post(input_text, mp4_path=None):
    try:
        if mp4_path:
            media_id = api.media_upload(mp4_path).media_id
            post_out = client.create_tweet(text=input_text, media_ids=[media_id])
        else:
            post_out = client.create_tweet(text=input_text)
        print(f"Twitter: Posted! Tweet ID: {post_out.data['id']}")
    except Exception as e:
        print(f"Twitter: Error during posting: {e}")

def d_post(input_text, channel_id):
    try:
        intents = discord.Intents.default()
        client = discord.Client(intents=intents)

        @client.event
        async def on_ready():
            channel = client.get_channel(DISCORD_CHANNEL_ID)
            if channel:
                await channel.send(input_text)
                print(f"Discord: Message sent to channel")
            await client.close()

        client.run(D_TOKEN)
    except Exception as e:
        print(f"Discord: Error during posting: {e}")


def twitter_run(input_text, mp4_path=None):
    verifyauthtwitter()
    t_post(input_text, mp4_path)

def discord_run(input_text):
    d_post(input_text)


def CommandLineRun():
    print("---------SET UP POST-----------")
    d_answer = input("Post to Discord (Y or N): ").strip().upper()
    t_answer = input("Post to Twitter (Y or N): ").strip().upper()
    discord_flag = d_answer == 'Y'
    twitter_flag = t_answer == 'Y'

    if discord_flag or twitter_flag:
        input_text = input("Text to Tweet/Discord: ")


        if discord_flag:
            print("--------------WITHIN DISCORD RUN-----------")
            link_answer = input("Add a link? (Y or N): ").strip().upper()
            if link_answer == 'Y':
                link_text = input("Enter the link: ").strip()
            discord_run(f"{input_text} {link_text}")

        mp4_path = None
        if twitter_flag:
            print("-------------WITHIN TWITTER RUN-----------")
            media_answer = input("Add Media? (Y or N): ").strip().upper()
            if media_answer == 'Y':
                media_exists_answer = input("Is the media already downloaded? (Y or N): ").strip().upper()

                if media_exists_answer == 'Y':
                    filename = input("Enter the media filename (without extension): ") + '.mp4'
                    mp4_path = os.path.join(OUTPUT_FOLDER, filename)
                else:
                    plat_answer = input("Which Platform is clip from (youtube or Twitch): (Y or T): ").strip().upper()
                    if plat_answer == 'T':
                        link_text = input("Enter the Twitch clip link: ")
                        filename = TwitchDownloadMain(link_text)
                        mp4_path = os.path.join(OUTPUT_FOLDER, filename)
                    if plat_answer == 'Y':
                        link_text = input("Enter the Youtube video link: ")
                        filename = YoutubeClipDownloadMain(link_text)
                        mp4_path = os.path.join(OUTPUT_FOLDER, filename)

            #twitter_run(input_text, mp4_path)


    print("----------SUCESSFULLY RAN MGBOT---------")
    return


if __name__ == '__main__':
   CommandLineRun()