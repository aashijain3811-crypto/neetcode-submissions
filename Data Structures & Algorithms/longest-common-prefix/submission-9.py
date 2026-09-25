class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word =strs[0]
        for i in range(len(word)):
            for j in strs:
                if i>=len(j)or word[i] !=j[i]:
                    return word[:i]

        return word            


        
       
            