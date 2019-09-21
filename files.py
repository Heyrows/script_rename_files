import os

import log
from log import initialLog
from log import logChanges

# Generic function to rename files
def renameFiles(src, dst, parsefunction):
    fileNames = os.listdir(src)
    # log the beginning of the task
    initialLog(len(fileNames))

    for filename in fileNames:
        newName = parsefunction(filename)

        locationSrc = src + '/' + filename
        locationDst = dst + '/' + newName
        os.rename(locationSrc, locationDst)
        # log when one file has been processed
        logChanges(filename, newName)