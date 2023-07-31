class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        my_map = {}
        List = []
        index = 0;
        Str = s[:len(p)]
        sortedp = sorted(p)
            
            
        for i in range(len(p) , len(s)+1):
           
            if sorted(Str) == sortedp :
                List.append(index)
                 
            
                 
            Str = s[index+1 : i+1]
            
            index += 1
            
        return List
                        
                
                
            