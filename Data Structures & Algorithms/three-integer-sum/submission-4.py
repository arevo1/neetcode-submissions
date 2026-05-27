def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
    
class Solution:        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = quick_sort(nums)
        res = set()
        

        for i,n1 in enumerate(nums_sorted):
            t = -n1
            seen = set()
            for j,n2 in enumerate(nums_sorted[i+1:]):
                c = t - n2
                if c in seen:
                    res.add(tuple((-t, c, n2)))
                seen.add(n2)
        
        sum3_list = [list(trip) for trip in res]

        return sum3_list

                    