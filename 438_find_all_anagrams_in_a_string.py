from typing import List


class Solution0:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls = len(s)
        lp = len(p)
        if ls < lp:
            return []
        res = []
        for i in range(0, ls - lp + 1):
            if res and res[-1] == i - 1 and s[i - 1] == s[i + lp - 1]:
                res.append(i)
                continue
            subs = s[i:i + lp]
            if self.judge_anagram(subs, p) is True:
                res.append(i)
        return res

    def judge_anagram(self, s1, s2):
        # print(s1,s2)
        map1 = {i: 0 for i in 'abcdefghijklmnopqrstuvwxyz'}
        for i, letter in enumerate(s1):
            map1[letter] += 1
        for j, letter in enumerate(s2):
            map1[letter] -= 1
            if map1[letter] < 0:
                return False
        for v in map1.values():
            if v != 0:
                return False
        return True


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls = len(s)
        lp = len(p)
        if ls < lp:
            return []
        mapp = {i:0 for i in 'abcdefghijklmnopqrstuvwxyz'}
        maps = {i:0 for i in 'abcdefghijklmnopqrstuvwxyz'}
        for w in p:
            mapp[w] += 1

        left = 0
        right = lp-1
        for w in s[left:right+1]:
            maps[w] += 1
        # print(maps)

        res=[]
        while right < ls:
            # print(left,right,s[left:right+1],res)
            map_res=self.compare_map(mapp,maps)
            if map_res == -1:  # 太少
                right+=1
                if right >=ls:
                    break
                maps[s[right]]+=1
            elif map_res == 1:
                maps[s[left]] -= 1
                left +=1
            else:
                res.append(left)
                # print(s[left], s[right])
                right+=1
                if right >=ls:
                    break
                maps[s[right]] += 1
                maps[s[left]] -= 1
                left+=1
                # print(s[left],s[right])

            # print(map_res)
        return res


    def compare_map(self,mp,ms):
        # print(f"{ms}")
        too_much=False
        for k in mp.keys():
            if mp[k] > ms[k]:
                return -1
            elif mp[k] < ms[k]:
                too_much=True
        if too_much==True:
            return 1
        else:
            return 0





if __name__ == "__main__":
    a = Solution()
    b = a.findAnagrams(s = "acdcaeccde", p = "c")
    print(b)