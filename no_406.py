from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        res=[]
        print(people)
        for i in people:
            if len(res) <= i[1]:
                res.append(i)
            else:
                res.insert(i[1],i)
        # print(res)
        return res



if __name__ == "__main__":
    a = Solution()
    b = a.reconstructQueue(people=[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])
    print(b)
