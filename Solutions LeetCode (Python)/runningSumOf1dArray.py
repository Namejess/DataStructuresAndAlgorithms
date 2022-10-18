# L'objectif est de retourner un array avec le traitement suivant : faire la somme de chaque entrée par l'entrée précédente
# Exemple [1,2,3,4] donnera [1,3,6,10] car [1, 1+2, 1+2+3, 1+2+3+4]
# Pour cela, on va parcourir le tableau, on va faire l'ajout de l'index -1 + l'index, afin de toujours additionner avec le bon index et la bonne valeur
#l'implémentation :
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        return nums



