from typing import List

class MagicDictionary:

    def __init__(self):
        self.m_dict = []

    def buildDict(self, dictionary: List[str]) -> None:
        self.m_dict = dictionary

    def search(self, searchWord: str) -> bool:
        for i in self.m_dict:
            res = self.check_match(i,searchWord)
            if res:
                return True
        return False

    def check_match(self,model_word,search_word):
        if len(model_word)!= len(search_word):
            return False
        diff_count=0
        for i in range(0,len(model_word)):
            if model_word[i] != search_word[i]:
                diff_count+=1
        if diff_count != 1:
            return False
        return True



if __name__ == "__main__":
    a = MagicDictionary()
    b = a.buildDict([["hello", "leetcode"]])
    c = a.search('')
    print(b)
    # passed