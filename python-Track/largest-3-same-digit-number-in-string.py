class Solution:
    def largestGoodInteger(self, num: str) -> str:
        myset = list()

        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                val = (num[i: i +3])
                print(val)
                myset.append(val)
            
        return (max(myset)) if myset else ""
        

        


