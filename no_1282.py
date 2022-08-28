from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_map = {}
        res = []
        for people, group_size in enumerate(groupSizes):
            if group_size==1:
                res.append([people])
                continue
            if group_map.get(group_size):
                group_map[group_size].append(people)
            else:
                group_map[group_size]=[people]
        # print(group_map)

        for k,v in group_map.items():
            while len(v)>0:
                res.append(v[:k])
                v = v[k:]
        return res

if __name__ == "__main__":
    a = Solution()
    b = a.groupThePeople(groupSizes = [3,3,3,3,3,1,3])
    print(b)


# AC