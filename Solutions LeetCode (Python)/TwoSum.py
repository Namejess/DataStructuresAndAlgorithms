# Solution pour le problème "Two Sum" de LeetCode
#
# Création d'un Hashmap pour faire qu'une passe de parcours de l'array en entrée.
# On récupère la différence entre la target (donnée en paramètre de l'exercice) et n (qui est la value de l'array récupéré) :
#  - Si on trouve cette différence dans la hashmap, on retourne le résultat
#  - Sinon on continue le parcours de l'array et on ajoute l'index i à n dans le hashmapSolution pour le problème "Two Sum" de LeetCode
#
# Création d'un Hashmap pour faire qu'une passe de parcours de l'array en entrée.
# On récupère la différence entre la target (donnée en paramètre de l'exercice) et n (qui est la value de l'array récupéré) :
#  - Si on trouve cette différence dans la hashmap, on retourne le résultat
#  - Sinon on continue le parcours de l'array et on ajoute l'index i à n dans le hashmap
#


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i

        return