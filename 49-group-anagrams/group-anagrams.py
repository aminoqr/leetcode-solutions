class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # go to every word in strs dict key is the sorted word "aet" : ["eat". "tea"]

        word_map = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            word_map[key].append(word)
        
        return [v for v in word_map.values()]
            

        