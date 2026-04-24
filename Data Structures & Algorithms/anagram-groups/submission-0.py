class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # keep a dictionary of anagram counter values, so we can index into it in 0(1) time for grouping
        # I can use the sorted strings as a key
        anagroups = dict()
        for word in strs:
            # print(word)
            sorted_word = "".join(sorted(word))
            # print(sorted_word)
            if sorted_word in anagroups:
                anagroups[sorted_word].append(word)
            else:
                anagroups[sorted_word] = [word]
        grouped = []
        for key, numList in anagroups.items():
            grouped += [numList]
        return grouped
            