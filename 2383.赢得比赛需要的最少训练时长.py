#
# @lc app=leetcode.cn id=2383 lang=python3
#
# [2383] 赢得比赛需要的最少训练时长
#

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int,
                         energy: List[int], experience: List[int]) -> int:
        need_exp = 0
        need_ene = initialEnergy
        total_match = len(energy)

        for i in range(total_match):
            need_ene = need_ene - energy[i]
            if initialExperience - experience[i] <= 0:
                need_exp = need_exp + (experience[i]+1 - initialExperience)
                initialExperience = experience[i]+1

            initialExperience = initialExperience + experience[i]
        print(need_ene, need_exp)
        if need_ene > 1:
            need_ene = 0
        else:
            need_ene = 1 - need_ene
        print(need_ene, need_exp)

        return need_ene + need_exp