# https://twitch-dl.bezdomni.net/installation.html

import os
import subprocess

def download_twitch_clip(link, output_folder, filename):
    try:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        output_path = os.path.join(output_folder, filename)
        subprocess.run(['twitch-dl', 'download', link, '-o', output_path], check=True)
        print(f"Download complete: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def TwitchDownloadMain(link):
    if link is None:
        link = input("Enter the Twitch clip link: ")

    filename = input("Enter the desired filename (without extension): ") + '.mp4'
    output_folder = r"C:\Users\squil\Downloads\THEMGBOT"
    file_path = os.path.join(output_folder, filename)

    download_twitch_clip(link, output_folder, filename)
    return filename, output_folder


if __name__ == "__main__":
    TwitchDownloadMain()


