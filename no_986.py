from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        f=0
        s=0
        res=[]
        while f < len(firstList) and s < len(secondList):
            # f = len(firstList)-1
            sub_interval=self.combine_interval(firstList[f],secondList[s])
            if not sub_interval:
                if firstList[f][1] <= secondList[s][1]:
                    f+=1
                else:
                    s+=1
                continue
            else:
                res.append(sub_interval)
                if firstList[f][1]<= secondList[s][1]:
                    f+=1
                else:
                    s+=1
                continue

        for i in range(1,len(res)):
            if res[i-1][1] == res[i][0]:
                interval=[res[i-1][0],res[i],[1]]
                del res[i-1]
                del res[0]
                res.insert(0,interval)
        return res

    # def combine_interval(self,f,s):
    #     max_start=max(f[0],s[0])
    #     min_end=min(f[1],s[1])
    #     if max_start <= min_end:
    #         return [max_start,min_end]
        return False

if __name__ == "__main__":
    a = Solution()
    b = a.intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]])
    print(b)

# AC