__author__ = 'sulla'
import os

def open_google_on_fingers_spread():
    import subprocess

    subprocess.call([r'C:\Program Files (x86)\Mozilla Firefox\Firefox.exe', '-new-tab',
                     'http://www.blastr.com/sites/blastr/files/1400308574-iron-man.jpg'])


def post_data_on_fist():
    import requests
    r = requests.get('http://jsonplaceholder.typicode.com/posts?userId=1')
    print r.content


def open_media_file():
    import os
    os.startfile('C:\Users\sulla\Videos\Spartan Race Super - Chicago 2014.mp4')


def create_file_on_wave_in():
    fileName = "C:\Users\sulla\Documents\myo\sample.txt"
    if os.path.isfile(fileName) is True:
        file_var = open(fileName, "w+")
        file_var.write("1")
        print "File Name:", file_var.name
        print "Closed :", file_var.closed


def create_file_on_wave_out():
    fileName = "C:\Users\sulla\Documents\myo\sample.txt"
    if os.path.isfile(fileName) is True:
        file_var = open(fileName, "w+")
        file_var.write("0")
        print "File Name:", file_var.name
        print "Closed :", file_var.closed


create_file_on_wave_in()
