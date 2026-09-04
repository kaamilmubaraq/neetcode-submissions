class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_array = [0] * 26

        for x,y in zip(s,t):
            char_array[ord(x) - ord('a')] += 1
            char_array[ord(y) - ord('a')] -= 1


        return all(z == 0 for z in char_array)
