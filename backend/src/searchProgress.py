from easydict import EasyDict as edict
progress = edict()
progress.imageCount = 0
progress.faceCount = 0
progress.matchCount = 0


def resetprogress():
    progress.imageCount = 0
    progress.faceCount = 0
    progress.matchCount = 0