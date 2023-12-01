class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        myhash = {}
        j = 1
        for i in order:
            myhash[i] = j
            j +=1

        for i in range(len(words)-1):
            temp = words[i]
            temp2 = words[i + 1]
            n = min(len(temp) , len(temp2))
            j = 0
            while j < n :
                if temp[j] == temp2[j]:
                    j+=1
                    continue
                elif temp[j] != temp2[j]:
                    if myhash[temp[j]] > myhash[temp2[j]]:
                        return False
                    else:
                         break
            else:
                if len(temp) > len(temp2):
                    return False
        
        return True



                



                