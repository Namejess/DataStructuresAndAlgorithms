# Cet exercice propose de trouver le "pivot index" dans un array donné en entrée.
# Si tous les nombres à gauche de l'index sont strictement égaux aux nombres à droite de l'index, alors on retourne la valeur de cet index
# Sinon, on retourne -1
# Ma 1ere intention était de parcourir l'array et d'ajouter dans un array nommé leftnum tous les nombres côté gauche grâce à un len(nums)/2
# Avec mes 2 array, je fais la somme grâce à sum(), et si c'est égal alors je retourne la valeur la plus à droite de mon array left (car c'est la valeur index du milieu)
# Sauf que le return -1 ne fonctionne pas. Je suis donc parti sur autre chose

# La solution est d'à nouveau utiliser un in enumerate() pour parcourir l'index/value et de directement prendre la somme total du tableau
# On calcule le côté droit du tableau - le côté gauche et - la valeur
# A chaque itération on vérifie si rightsum et leftsum sont égaux, puis on itère et on ajout value à leftsum
# Si ils le sont alors on renvoie l'index, sinon on poursuit. Et si aucun n'est trouvé, alors on retourne -1

#----------------SOLUTION COMPLETE--------------

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum = 0
        totalsum = sum(nums)

        for i, value in enumerate(nums):
            rightsum = totalsum - leftsum - value

            if rightsum == leftsum:
                return i

            leftsum += value

        return -1


#----------SOLUTION INCOMPLETE--------------
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        leftnum = []
        rightnum = []

        for i in range(len(nums)):
            if i < len(nums) / 2:
                leftnum.append(nums[i])
            else:
                rightnum.append(nums[i])

            sum1 = sum(leftnum)
            sum2 = sum(rightnum)

            if sum1 == sum2 and len(nums) % 2 == 0:
                return leftnum[-1]

            else:
                return -1


