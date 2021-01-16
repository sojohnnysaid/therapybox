import requests
import os


def download(url, filename, headers):
    cwd = os.getcwd()
    url = url
    file = requests.get(url, headers=headers)
    open(f'{cwd}/{filename}', 'wb').write(file.content)
