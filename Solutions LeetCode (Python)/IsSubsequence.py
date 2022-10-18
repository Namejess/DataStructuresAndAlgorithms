# Pour trouver si s est un subsequence de t, on compare chaque lettre des 2 strings avec 2 pointeurs
# i et j, tant qu'il sont pas à la fin, on réalise un traitement
# On compare la 1ere lettre, si elles matchent on incremente.
# Si la lettre est différente, on incrémente QUE j.


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return True if i == len(s) else False
