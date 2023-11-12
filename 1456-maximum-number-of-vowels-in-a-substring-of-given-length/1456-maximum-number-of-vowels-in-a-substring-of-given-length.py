class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        arr = [ 'a' , 'e' , 'i' , 'o'   , 'u']
        counter = 0
        
        ss = list(s)
        
        win = deque()
        maxval = 0 
        
        for i in range(len(ss)):
            win.append(ss[i])
            if i < k:
                if ss[i] in arr:
                    counter +=1
            
            if len(win) > k:
                x = win.popleft()
                if x in arr and ss[i] in arr:
                    continue
                elif x not in arr and ss[i] in arr:
                    counter += 1
                elif x in arr and ss[i] not in arr:
                    counter -= 1
                
            
            if len(win) == k:
                maxval = max(counter , maxval)
                
        return maxval
                        
                
            
            