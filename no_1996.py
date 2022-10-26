from typing import List
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0],x[1]))
        print(properties)
        res = 0
        for character in properties:
           pass 

if __name__ == '__main__':
    a = Solution()
    b = a.numberOfWeakCharacters([[1,5],[10,4],[4,3]])
    print(b)
        