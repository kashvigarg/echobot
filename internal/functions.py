import requests
import os

async def check_size(file_size):
    file_size_in_mb = file_size / 1048576
    if (file_size_in_mb) > 25:
        return file_size_in_mb, False
    else :
        return file_size_in_mb, True
    
async def download_file(file_path, file_name):
    media_directory = 'media'
    if not os.path.exists(media_directory):
        os.makedirs(media_directory)

    downloaded_media = requests.get(file_path)
    with open(os.path.join(media_directory, file_name), 'wb') as f:
        f.write(downloaded_media.content)

async def delete_file(file_name):
    media_directory = 'media'
    if not os.path.exists(f"{media_directory}/{file_name}"):
        print("File or directory doesn't exist")
    else:
        os.remove(f"{media_directory}/{file_name}")


from pytube import YouTube

async def download_youtube_audio(url, output_path='media'):
    try:
        youtube = YouTube(url)
        audio_stream = youtube.streams.filter(only_audio=True, file_extension='mp4').first()
        audio_stream.download(output_path, filename='yt.mp4')

       
        await delete_file(audio_stream.title)
        return True, audio_stream.title, audio_stream.filesize
    except Exception as e:
        return False, '' , 0
