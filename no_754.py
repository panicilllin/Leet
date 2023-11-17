class Solution:
    def reachNumber(self, target: int) -> int:
        ans=0
        road=0
        target = abs(target)
        while road < target:
            ans+=1
            road+=ans
        print(road,ans)
        if road == target:
            return ans
        elif (road - target) % 2 == 0:
            return ans
        else:
            if ans % 2 == 0:
                return ans+1
            else:
                return ans+2
            
            
        
if __name__ =="__main__":
    a = Solution()
    b = a.reachNumber(4)
    print(b)


# AC