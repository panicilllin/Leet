from typing import List


class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.hash_dict={}
        for i in range(0,len(self.words)):
            word = self.words[i]
            for j in range(1,len(word)+1):
                for k in range(1,len(word)+1):
                    pref = word[:j]
                    suff = word[-k:]
                    h_key = pref + '-' + suff
                    self.hash_dict[h_key] = i

    def f0(self, pref: str, suff: str) -> int:
        for i in range(len(self.words)-1, -1,-1):
            # print(self.words[i][:len(pref)])
            # print(self.words[i][-len(suff):])
            if self.words[i][:len(pref)] != pref:
                continue
            elif self.words[i][-len(suff):] != suff:
                continue
            else:
                return i
        return -1

    def f(self, pref: str, suff: str) -> int:
        h_key = pref + '-' + suff
        print(h_key)
        print(self.hash_dict)
        try:
            return self.hash_dict[h_key]
        except:
            return -1
        # if self.hash_dict.get(h_key):
        #     return self.hash_dict[h_key]
        # else:
        #     return -1

if __name__ == "__main__":
    a = WordFilter(['apple'])
    b = a.f('a', 'e')
    print(b)