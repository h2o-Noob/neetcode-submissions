class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for items in strs:
            hash_map[''.join(sorted(items))].append(items)
        return list(hash_map.values())
        