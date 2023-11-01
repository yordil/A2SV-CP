class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        stud = deque(students)
        san = deque(sandwiches) 
        left = 0
        answer= 0
        while san:
            
            
            if stud[0] != san[0]:
                stud.append(stud.popleft())
                
            else:
                answer +=1
                stud.popleft()
                san.popleft()
                
            if all(s != san[0] for s in stud):
                break
                
        return len(students) - answer
                
                