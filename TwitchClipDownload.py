# https://twitch-dl.bezdomni.net/installation.html

import os
import subprocess
from dotenv import load_dotenv

load_dotenv("keys.env")

OUTPUT_FOLDER = os.getenv('OUTPUT_FOLDER')

def download_twitch_clip(link, filename):
    try:
        if not os.path.exists(OUTPUT_FOLDER):
            os.makedirs(OUTPUT_FOLDER)
        output_path = os.path.join(OUTPUT_FOLDER, filename)
        subprocess.run(['twitch-dl', 'download', link, '-o', output_path], check=True)
        print(f"Download complete: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def TwitchDownloadMain(link_text):
    if link_text is None:
        link_text = input("Enter the Twitch clip link: ")

    filename = input("Enter the desired filename (without extension): ") + '.mp4'
    file_path = os.path.join(OUTPUT_FOLDER, filename)

    download_twitch_clip(link_text, filename)
    return filename


if __name__ == "__main__":
    TwitchDownloadMain()


