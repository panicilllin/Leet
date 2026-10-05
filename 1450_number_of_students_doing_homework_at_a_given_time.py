from typing import List

class Solution0:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        start_list=[]
        for i,start_time in enumerate(startTime):
            if start_time <= queryTime:
                start_list.append(i)
        res=0
        for student in start_list:
            if endTime[student]>= queryTime:
                res+=1
        return res

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        res=0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime and endTime[i] >= queryTime:
                res+=1
        return res