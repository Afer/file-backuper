import shutil
import os
import sys
from os.path import isfile

#set root paths here
backupSource = './source/'
backupDest = './dest/'

# set ignored folder names here. Only works with folder names
ignorePaths = ['node_modules', 'ggez', 'mine', 'mine-back', 'mining', 'Switch', 'file-encryptor', 'goob', 'goob-bak', 'goob-v2', 'magic-mirror', 'mimic', 'pid', 'Randinger', 'tomcat8', 'Youtube-DLG']

hasFiles = False
dirListCheck = os.listdir(backupSource)
for any in dirListCheck:
    hasFiles = True
    break

if not hasFiles:
    input("No files to encrypt, press Enter to continue.")
    sys.exit(-1)

def recursiveBackup(dir):
    #print ("starting relative dir " + dir)

    dirList = os.listdir(backupSource + dir)
    funcRoot = backupSource + dir

    for fileName in dirList:
        fullPath = funcRoot + fileName

        if fileName in ignorePaths:
            continue

        if not isfile(fullPath):
            recursiveBackup(dir + fileName + "/")
            continue

        #print("Path: " + fullPath)

        fullPathSplit = fullPath[len(backupSource):].split("/")
        destPath = backupDest + "/".join(fullPathSplit)

        #print("Path: " + destPath)
        #print(os.path.getmtime(filename))

        if not isfile(destPath):
            os.makedirs(os.path.dirname(destPath), exist_ok=True)
            with open(destPath, 'w+') as tempNewFile:
                print("Creating new file: " + destPath)

        # not needed if last modified timestamps match
        if os.path.getmtime(fullPath) == os.path.getmtime(destPath):
            print("No Updates: " + fullPath)
            continue

        print("Copying... ", fullPath, os.path.getmtime(fullPath), os.path.getmtime(destPath))

        shutil.copy2(fullPath, destPath)
    
    #print ("Finished dir " + dir)

recursiveBackup("")