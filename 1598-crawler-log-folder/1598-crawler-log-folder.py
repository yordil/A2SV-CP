class Solution:
    def minOperations(self, logs: List[str]) -> int:
        st = []

        for lg in logs:
            if lg != './':
                if lg != '../':
                    st.append(lg)
                else:
                    if st:
                        st.pop()
        return len(st)



#  my previous implmetation


# class Solution:
#     def minOperations(self, logs: List[str]) -> int:
        
#         st = []
#         counter = 0
        
#         for i in range(len(logs)):
            
#             if logs[i] == "./":
#                 continue
#             elif st and logs[i] == "../":
#                 st.pop()
#             elif logs[i] != "../" and logs[i] != "./" :
#                 st.append(logs[i])
        
#         return len(st)
                
            
            
            