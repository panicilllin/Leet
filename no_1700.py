from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        

        while len(sandwiches)>0:
            flg = False
            for i in range(len(students)):

                if len(sandwiches) == 0:
                        break
                if students[i] == sandwiches[0]:
                    students[i]=None
                    sandwiches.pop(0)
                    flg = True
                else:
                    continue
            if flg == False:
                break
        res=0
        for i in students:
            if i != None:
                res+=1
        return res
     
     
     
if __name__ =="__main__":
    a = Solution()
    b = a.countStudents([1,1,0,0],[0,1,0,1])
    print(b)