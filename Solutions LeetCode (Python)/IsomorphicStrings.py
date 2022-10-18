class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        hashmap = {}
        hashset = {}
        c1 = 0
        c2 = 0

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            if c1 in hashmap:
                if c1 != c2:
                    return False
                else:
                    if c2 in hashset:
                        return False
            hashset.add(c2)

            c2 = hashset(c2)
            hashmap = {c1:c2}

            hashmap.put(c1, c2)
            hashset.add(c2)

