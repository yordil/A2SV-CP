class Solution:
    def reverseStr(self, s: str, k: int) -> str:
            # Convert the string to a list of characters to make it mutable
        s = list(s)
        n = len(s)

        for i in range(0, n, 2 * k):
            # Reverse the first 'k' characters if there are at least 'k' characters left
            s[i:i+k] = reversed(s[i:i+k])

        return ''.join(s)
        # return
        