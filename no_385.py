# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
        """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

    def isInteger(self):
        """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

    def add(self, elem):
        """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

    def setInteger(self, value):
        """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

    def getInteger(self):
        """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

    def getList(self):
        """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stack = [NestedInteger()]
        # res = NestedInteger()
        # s_list = s.split(',')
        # now_list = NestedInteger()
        word = ''
        for i in s:

            if i == '[':
                nestl = NestedInteger()
                stack.append(nestl)
            elif i == '-':
                pass
            elif i == ',':
                word = ''
                stack[-1].add(int(word))
            elif i == ']':
                word = ''
                nest_now = stack.pop()
                stack[-1].add(nest_now)
            else:
                word += i
        if word != '':
            stack[-1].add(word)
        return stack[-1]

if __name__ == "__main__":
    a = Solution()
    b = a.deserialize("[123,aaa,[456,[789,101]]]")
    print(b)
