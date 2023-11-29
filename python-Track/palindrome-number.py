class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        arr = []
        while x:
            arr.append(x%10)
            x //=10

        l , r   = 0 , len(arr)-1

        while l <=r:
            if arr[l] == arr[r]:
                l+=1
                r-=1
            else:
                print(arr)
                return False

        return True