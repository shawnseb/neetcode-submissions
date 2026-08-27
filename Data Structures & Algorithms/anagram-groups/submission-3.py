import copy
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        world = dict()
        for string in strs:
            inter = copy.deepcopy(string)
            inter = sorted(inter)
            if str(inter) in world:
                world[str(inter)].append(string)
            else:
                world[str(inter)] = [string]
        answer = []
        for sets in world:
            answer.append(world[sets])
        return answer
        