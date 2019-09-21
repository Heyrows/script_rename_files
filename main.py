import files
from files import renameFiles

import arc
from arc import Arc
from arc import ArcCollection

# Source and destination folder, they can be the same
src = './sample'
dst = './dist'

# Example of collection
ArcsOnePiece = ArcCollection('One Piece', [
    Arc(1, 3, 'Romance Dawn'),
    Arc(4, 8, 'Baggy le Clown'),
    Arc(9, 17, 'Capitaine Kuro'),
    Arc(18, 30, 'Baratie'),
    Arc(31, 45, 'Arlong'),
    Arc(46, 47, 'Les aventures a Baggy'),
    Arc(48, 53, 'Loguetown'),
    Arc(54, 61, 'Ile du Navire de Guerre'),
    Arc(61, 63, 'Laboon'),
    Arc(64, 67, 'Whiskey Peak'),
    Arc(68, 69, 'Koby & Hermep'),
    Arc(70, 77, 'Little Garden'),
    Arc(78, 91, 'Royaume de Drum'),
    Arc(92, 130, 'Alabasta'),
    Arc(131, 135, 'Post-Alabasta'),
    Arc(136, 138, 'Ile des Chevres'),
    Arc(139, 143, 'Brume Arc-en-Ciel'),
    Arc(144, 152, 'Jaya'),
    Arc(153, 195, 'Skypiea'),
    Arc(196, 206, 'G-8'),
    Arc(207, 219, 'Davy Back Fight'),
    Arc(220, 224, 'Le Voleur de Memoire'),
    Arc(225, 228, 'Le Retour de Foxy'),
    Arc(229, 263, 'Water Seven'),
    Arc(264, 312, 'Enies Lobby'),
    Arc(313, 325, 'Post-Enies Lobby'),
    Arc(326, 335, 'Chasseurs de Glace'),
    Arc(337, 381, 'Thriller Bark'),
    Arc(382, 384, 'Ile de Spa'),
    Arc(385, 405, 'Sabaody'),
    Arc(408, 421, 'Amazon Lily'),
    Arc(422, 425, 'Impel Down'),
    Arc(426, 429, 'Des Nouvelles de l\'equipage'),
    Arc(430, 452, 'Impel Down'),
    Arc(453, 456, 'Des Nouvelles de l\'equipage'),
    Arc(457, 489, 'Marineford'),
    Arc(490, 516, 'Post-Marineford')
])

# Example of parsing function
def parseOnePieceFileName(filename):
    splitNameExtension = filename.split('.')
    splitOldName = splitNameExtension[0].split(' ')
    splitMinMax = splitOldName[2].split('-')
    min = int(splitMinMax[0])
    index = int(splitOldName[-1]) - 1

    extension = splitNameExtension[1]
    episodeNumber = min + index
    arcName = ArcsOnePiece.findArcName(episodeNumber)

    newName = 'One Piece ' + str(episodeNumber) + ' - Arc ' + arcName + '.' + extension
    return newName

renameFiles(src, dst, parseOnePieceFileName)