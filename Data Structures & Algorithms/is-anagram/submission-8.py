class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        world = dict()
        for i in s:
            if i not in world:
                world[i] = 0
            world[i] = world[i] + 1
        for i in t:
            if i not in world:
                return False
            world[i] = world[i] - 1
            if world[i] < 0:
                return False
        return True
