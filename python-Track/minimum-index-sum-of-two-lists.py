from collections import defaultdict
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        collector = defaultdict(list)
    
        for i in range(len(list1)):
            if list1[i] not in list2:
                continue
            else:
                collector[i+list2.index(list1[i])].append(list1[i])
                
        minval = min(collector.keys())
        
        return collector[minval]
       
        