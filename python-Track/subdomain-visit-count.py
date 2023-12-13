class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        myhash ={}
        
        for i in range(len(cpdomains)):
            temp = cpdomains[i]
            arr = temp.split(" ")
            count = int(arr[0])
            arr.remove(arr[0])
            S = arr[0]
            arr2 = S.split(".")
            first = arr2[len(arr2)-2]
            first+="."
            first+=arr2[len(arr2)-1]
            second = arr2[len(arr2)-1]
            
            myhash[first] = myhash.get(first , 0) + count
            myhash[second] = myhash.get(second , 0) + count
            if len(arr2) ==3:
                myhash[S] = myhash.get(S,0) + count
            
            
        ans = [f"{v} {i}" for i , v in myhash.items()]
        print(ans)
        
    
        return ans
            
            
            
            