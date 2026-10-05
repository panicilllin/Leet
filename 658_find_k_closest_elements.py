from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        beg=0

        for i, num in enumerate(arr):
            beg = i
            if num >= x:
                break
        res=[]
        arr1=arr[:beg]
        arr2=arr[beg:]
        while len(res)<k:
            if arr1 and arr2:
                if abs(arr1[-1] - x) < abs(arr2[0] - x)\
                    or abs(arr1[-1] - x) == abs(arr2[0] -x) and arr1[-1] < arr2[0]:
                    res.append(arr1.pop(-1))
                else:
                    res.append(arr2.pop(0))
            elif  arr1:
                res.append(arr1.pop(-1))
            else:
                res.append(arr2.pop(0))
        res.sort()
        return res


from typing import List

class Solution2:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        point=0
        for i, num in enumerate(arr):
            point = i
            if num >= x:
                break
        beg = point
        end = point
        while end-beg<k:
            if beg>0 and end < len(arr):
                a = arr[beg-1]
                b = arr[end]
                if abs(a-x) < abs(b-x) or abs(a-x)==abs(b-x):
                    beg-=1
                else:
                    end+=1
            elif beg>0:
                beg-=1
            else:
                end+=1
        return arr[beg:end]