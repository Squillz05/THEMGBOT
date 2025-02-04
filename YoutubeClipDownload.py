import yt_dlp
import os
from dotenv import load_dotenv


load_dotenv("keys.env")

OUTPUT_FOLDER = os.path.normpath(os.getenv('OUTPUT_FOLDER'))

def youtube_download(youtube_url,filename):
    try:
        ydl_opts = {
            'format': 'bestvideo[height<=1080]+bestaudio[ext=m4a]/bestaudio',
            'outtmpl': os.path.join(OUTPUT_FOLDER, filename),
            'merge_output_format': 'mp4',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])

        print(f"Downloaded file: {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def YoutubeDownloadMain(link_text):
    if link_text is None:
        link_text = input("Enter the Youtube URL: ")

    filename = input("Enter the name for the file (without extension): ") + '.mp4'
    youtube_download(link_text,filename)
    return filename

def YoutubeClipDownloadMain(link_text):
    if link_text is None:
        link_text = input("Enter the Youtube URL: ")

    filename = input("Enter the name for the file (without extension): ") + '.mp4'
    youtube_download(link_text, filename)
    return  filename


if __name__ == "__main__":
    clip_answer = input("Clip or Full Video:? (C or F): ")

    if clip_answer == 'F':
        YoutubeDownloadMain(link_text=None)
    if clip_answer == 'C':
        YoutubeClipDownloadMain(link_text=None)

