from typing import List

class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs
    
    def quickSortHelper(self, arr: List[Pair], s: int, e: int) -> None:
        #  get the pivot
        if e - s + 1 <= 1:
            return 
        
        pivot = arr[e]
        left = s


        for i in range(s, e):
            if arr[i].key < pivot.key:
                tmp = arr[left]
                arr[left] = arr[i]
                arr[i] = tmp
                left += 1
        
        arr[e] = arr[left]
        arr[left] = pivot

        self.quickSortHelper(arr, s, left - 1)
        self.quickSortHelper(arr, left + 1, e)
