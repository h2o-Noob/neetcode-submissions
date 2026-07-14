class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_m = defaultdict(list)

        for items in strs:
            hash_m[''.join(sorted(items))].append(items)
        return list(hash_m.values())