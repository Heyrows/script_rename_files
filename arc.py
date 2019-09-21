import sys

class Arc:
    def __init__(self, firstEpisode, lastEpisode, name):
        self.firstEpisode = firstEpisode
        self.lastEpisode = lastEpisode
        self.name = name
        self.__ensureArc()

    def __ensureArc(self):
        try:
            if self.firstEpisode > self.lastEpisode:
                raise RuntimeError('Wrong Instantiation of Arc: ' + self.name)
        except Exception, err:
            sys.stderr.write('%s\n' % str(err))
            sys.exit(1)

class ArcCollection:
    def __init__(self, name, arcList):
        self.name = name
        self.collection = arcList
        self.__ensureCollection()

    def findArcName(self, episodeNumber):
        for arc in self.collection:
            if arc.firstEpisode <= episodeNumber <= arc.lastEpisode:
                return arc.name

    def __ensureCollection(self):
        currentEpisodeNumber = 0
        for arc in self.collection:
            try:
                if arc.firstEpisode < currentEpisodeNumber:
                    raise RuntimeError('Wrong Index: collection -> ' + self.name + ' | arc -> ' + arc.name)
                if currentEpisodeNumber > arc.lastEpisode:
                    raise RuntimeError('Wrong Index: collection -> ' + self.name + ' | arc -> ' + arc.name)
                currentEpisodeNumber = arc.lastEpisode
 
            except Exception, err:
                sys.stderr.write(str(err) + '\n')
                sys.exit(1)
