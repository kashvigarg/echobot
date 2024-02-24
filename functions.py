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
        