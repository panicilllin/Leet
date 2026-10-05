from collections import OrderedDict
from typing import List
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=lambda x: (len(x), x))
        sentence = sentence.split(' ')
        res=''
        for word in sentence:
            flag=True
            for k in dictionary:
                # print(f"w={word},k={k}, res={res}")
                if len(k) > len(word):
                    res += word + ' '
                    flag = False
                    break
                elif word[:len(k)] == k:
                    res += k + ' '
                    flag = False
                    break
                else:
                    continue
            if flag:
                res += word + ' '
        return res[:-1]





if __name__ == "__main__":
    a = Solution()
    b = a.replaceWords(dictionary =["cat","bat","rat"], sentence = "the cattle was rattled by the battery")
    print(b)
    # passed

