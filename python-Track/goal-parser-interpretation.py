class Solution:
    def interpret(self, command: str) -> str:
        if len(command) == 1:
            return command
        ans = ""
        stack = []

        i  = 0 
        for i in range(len(command) - 1):
            if command[i] == "(" and command[i+1] ==")":
                ans += "o"
            elif command[i].isalpha():
                ans+=command[i]
        
        if command[i+1].isalpha():
            ans+=command[i+1]
            return ans
       
        return ans
      
        # for c in command:
        #     if stack and stack[-1] == "(":
        #         if c == ")":
        #             ans+="o"
        #         else:
        #              ans+=i
