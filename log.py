def initialLog(numberOfFiles):
    print('---- BEGINNING RENAMING ----')
    print('  Going to rename %s files \n' % numberOfFiles)

def logChanges(oldName, newName):
    print('---- File successfully renamed ---- ')
    print('  %s\n <- has become -> \n%s\n\n' % (oldName, newName))