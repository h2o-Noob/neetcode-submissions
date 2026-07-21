class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_map = defaultdict(list)

        for w in strs:
            hash_map[''.join(sorted(w))].append(w)
        return list(hash_map.values())
        
        