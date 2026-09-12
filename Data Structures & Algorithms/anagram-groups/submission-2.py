class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}

        for w in strs:
            sorted_w = tuple(sorted(w))
            if sorted_w in store:
                store[sorted_w].append(w)
            else:
                store[sorted_w] = [w]
        
        return list(store.values())