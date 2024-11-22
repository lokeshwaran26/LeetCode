class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        print(anagram_map)

        for word in strs:
            sorted_word = "".join(sorted(word))
            anagram_map[sorted_word].append(word)

        print(anagram_map.values())
        return list(anagram_map.values())
