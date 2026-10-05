class Solution:

    def predictPartyVictory0(self, senate: str) -> str:
        if 'D' not in senate:
            return 'Radiant'
        if 'R' not in senate:
            return 'Dire'
        R_list = 0
        D_list = 0
        vote_right = [1]*len(senate)
        # print(vote_right)
        
        for i in range(0, len(senate)):
            print('----')
            print(i, senate[i], R_list,D_list)
            if senate[i] == 'R' and D_list > 0:
                vote_right[i] = 0
                D_list -= 1
            elif senate[i] == 'R' and D_list == 0:
                R_list += 1
            elif senate[i] == 'D' and R_list > 0:
                vote_right[i] = 0
                R_list -= 1
            elif senate[i] == 'D' and R_list == 0:
                D_list += 1
            print(senate[i], vote_right[i])
        new_senate = ''
        
        for i in range(0, len(senate)):
            if vote_right[i] == 1:
                new_senate += senate[i]
        print(new_senate)
        res = self.predictPartyVictory(new_senate)
        return res

    def predictPartyVictory(self, senate: str) -> str:
        R_list = []
        D_list = []
        n = len(senate)
        for i in range(0,len(senate)):
            if senate[i] =='R':
                R_list.append(i)
            else:
                D_list.append(i)
        while len(R_list)!= 0 and len(D_list) !=0:
            if R_list[0] < D_list[0]:
                n+=1
                R_list.append(n)
            else:
                n+=1
                D_list.append(n)
            R_list.pop(0)
            D_list.pop(0)
        return "Dire" if len(R_list) ==0 else "Radiant"
        
if __name__ == "__main__":
    a = Solution()
    b = a.predictPartyVictory('RDRD')
    print(b)