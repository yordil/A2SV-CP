class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [0] * len(s)

        for i in range(len(indices)):
            ans[indices[i]] = s[i]

        return "".join(ans)
       
       
       
       
       
       
       
       
       
        # myhash = {}
        # arr = s.split()
        # for i in range(len(s)):
        #     myhash[s[i]]  = indices[i]

        # def customcomparator(item):
        #     return myhash[item]
        # arr.sort(key=customcomparator)

        # return "".join(arr)

        