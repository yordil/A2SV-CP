class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        dictionary = defaultdict(list)

        for word in strs:

            curr = "".join(sorted(word))

            print(curr)
            dictionary[curr].append(word)

        ans = list(dictionary.values())
       
        return ans 