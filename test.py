__author__ = 'sulla'


def open_google_on_fingers_spread():
    import subprocess

    subprocess.call([r'C:\Program Files (x86)\Mozilla Firefox\Firefox.exe', '-new-tab', 'http://www.monkeybars.io/'])


def post_data_on_fist():
    import requests

    r = requests.get('http://jsonplaceholder.typicode.com/posts?userId=1')
    print r.content


def open_media_file():
    import os

    os.startfile('C:\Users\sulla\Videos\Spartan Race Super - Chicago 2014.mp4')


open_media_file()
