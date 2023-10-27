class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        myhash = {}
        
        for num in nums:
            if num in myhash:
                myhash[num]  +=1
            else:
                myhash[num] = 1
        ans =[]
        
        for i in range(k):
            max_key = max(myhash, key=myhash.get)

            ans.append(max_key)

            del myhash[max_key]
            
        return ans