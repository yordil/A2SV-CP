class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        
        hashmap = defaultdict(list)
        
        for path in paths:
            first_path = path.split()
            directory = first_path[0]
            
            for f in first_path[1:]:
                temparr = f.split("(")
                myfilename = temparr[0]
                myinnerfile = temparr[1]
                
                fullpath = directory + "/" + myfilename
                hashmap[myinnerfile].append(fullpath)
            
        ans = [val for val in hashmap.values() if len(val) > 1]
        
        return ans
            