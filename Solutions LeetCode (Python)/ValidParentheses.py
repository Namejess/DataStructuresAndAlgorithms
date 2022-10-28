class Solution:
    def isValid(self, s: str) -> bool:

        hashmap = {")": "(", "]": "[", "}": "{"}
        stack = []

        for i in s:
            print(i)
            if i in hashmap:
                print(i)
                if stack and stack[-1] in hashmap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False
