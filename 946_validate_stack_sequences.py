from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i=0
        j=0
        while i <len(pushed) or j < len(popped):
            if stack and stack[-1] == popped[j]:
                stack.pop()
                j+=1
            elif i < len(pushed):
                num = pushed[i]
                stack.append(num)
                i+=1
            else:
                return False
        
        if j < len(popped)-1:
            return False
        return True 
        
if __name__ == '__main__':
    a = Solution()
    b=a.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,2,1])
    print(b)

# AC