class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # go to every word in strs dict key is the sorted word "aet" : ["eat". "tea"]

        word_map = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in word_map:
                word_map[key] = [word]
            else:
                word_map[key].append(word)
        
        return [value for value in word_map.values()]
            

        