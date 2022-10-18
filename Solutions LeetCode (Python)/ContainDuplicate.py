# L'objectif est de déterminer s'il existe un doublon dans un array donné en entrée.
# Plusieurs solutions : passer plusieurs fois dans le tableau, ce qui augmente la complexité
# La solution la plus efficace est de faire qu'une seule passe, en utilisant un hashSet
# On ajoute n dans le hashset et s'il est déjà existant à l'intérieur, on retourne True car cela veut dire qu'il y a un doublon

from typing import List


def containDuplicate(self, nums: List[int]):

    hashset = set()

    for i in nums :
        if i in hashset:
            return True
    hashset.add(i)
    return False

