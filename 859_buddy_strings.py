class Solution:
    def buddyStrings_old(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        leng = len(s)
        for i in range(leng):
            # print(i)
            for j in range(i+1, leng):
                s_l = [i for i in s]
                a = s_l[i]
                s_l[i] = s[j]
                s_l[j] = a
                s_new =''.join(s_l)
                # print(f"s_new: {i,j,s_new}")
                if s_new == goal:
                    return True
        return False

    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        leng = len(s)
        if s == goal:
            s_l = [i for i in s]
            s_l2 = list(set(s_l))
            if len(s_l2) < leng:
                return True
        swap = []
        for i in range(leng):
            if s[i] != goal[i]:
                swap.append([s[i],goal[i]])
        print(swap)
        if len(swap) == 2 and swap[0][0] == swap[1][1] and swap[0][1] == swap[1][0]:
            return True
        return False


a = Solution()
b = a.buddyStrings("aa","aa")
print(b)