import os
import sys
import time

if (len(sys.argv) > 1):
    file_path = sys.argv[1]
    file1 = open(file_path, 'r')
    lines = file1.readlines()

    for line in lines:
        time.sleep(5)
        os.system("youtube-dl --extract-audio --audio-format mp3 " + line)
else:
    print("Zu wenig Argumente. (Dateipfad fehlt)")
