class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        partitions = []
        i = 0

        while i < len(s):
            char = s[i]
            last_occurrence = s.rfind(char)

            j = i + 1
            while j < last_occurrence:
                last_occurrence = max(last_occurrence, s.rfind(s[j]))
                j += 1

            partitions.append(last_occurrence - i + 1)
            i = last_occurrence + 1

        return partitions
            
        
        