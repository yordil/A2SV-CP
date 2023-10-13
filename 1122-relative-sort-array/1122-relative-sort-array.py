class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        # Create a dictionary to map elements in arr2 to their positions
        position = {num: i for i, num in enumerate(arr2)}
        
        # Sort arr1 based on the positions of elements in arr2
        arr1.sort(key=lambda x: (position.get(x, len(arr2)), x))
        
        return arr1