class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        newlist = []
        
        for i in range (len(operations)):
            
            if operations[i] == "+":
                newlist.append(int(newlist[-1] + newlist[-2] ))
            elif operations[i] == "D":
                 newlist.append(int(2 * newlist[-1] ))
            elif operations[i] == "C":
                 newlist.pop()
            else:
                newlist.append(int(operations[i]))
               
        return sum(newlist)