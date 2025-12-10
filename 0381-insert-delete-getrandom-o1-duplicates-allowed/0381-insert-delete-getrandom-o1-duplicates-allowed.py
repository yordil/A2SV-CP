class RandomizedCollection:

    def __init__(self):
        self.arr = []              
        self.idx = {}              

    def insert(self, val: int) -> bool:
        existed = val in self.idx
        
        if not existed:
            self.idx[val] = set()

        self.idx[val].add(len(self.arr))
        self.arr.append(val)
        
        return not existed

    def remove(self, val: int) -> bool:
        if val not in self.idx or len(self.idx[val]) == 0:
            return False
        
    
        remove_idx = self.idx[val].pop()
        
        last_val = self.arr[-1]
        last_idx = len(self.arr) - 1

     
        if remove_idx != last_idx:
            self.arr[remove_idx] = last_val
            
    
            self.idx[last_val].remove(last_idx)
            self.idx[last_val].add(remove_idx)

    
        self.arr.pop()


        if len(self.idx[val]) == 0:
            del self.idx[val]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
