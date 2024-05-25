import random
from fonctions_geo import *
from recherche_par_nom import *
from matching_keyword import *
from recherche_autre import *
from voice_engine import *

if __name__ == '__main__':
    texte = voiceCity()
    texte = find_city(texte)
    print(texte)