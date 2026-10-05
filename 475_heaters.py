from typing import *
class Solution_old:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses = list(set(houses)).sort()
        heaters = list(set(heaters)).sort()
        houses = [i for i in houses if i not in heaters]
        if not houses:
            return 0
        # heat_circle = 1
        # if len(houses) == 1 and len(heaters)==1:
        #     cir_max = abs(heaters-houses)
        # elif len(houses) <= 1:
        #     cir_max = max(abs(max(heaters) - houses),abs(min(heaters)-houses))
        # elif len(heaters) <= 1:
        #     cir_max = max(abs(max(houses) - heaters), abs(min(houses) - heaters))
        # else:
        #     cir_max = max(abs(max(houses)-min(heaters)),abs(max(heaters)-min(houses)))
        # print(f"cir_max=={cir_max}")
        while heat_circle <= 1e9:
            for item in heaters:
                print(f"cir={heat_circle}")
                print(f"heater==={item}")
                print(houses)
                min_heat = item - heat_circle
                max_heat = item + heat_circle
                print(f"max={max_heat},min={min_heat}")
                if min_heat in houses:
                    houses.pop(houses.index(min_heat))
                if max_heat in houses:
                    houses.pop(houses.index(max_heat))
                if len(houses) == 0:
                    return heat_circle
            heat_circle +=1
        return heat_circle

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses = [i for i in houses if i not in heaters]
        if not houses:
            return 0
        houses = list(set(houses))
        houses.sort()
        heaters = list(set(heaters))
        heaters.sort()

        house_dict = {}
        min_circle = 0
        for i in houses:
            if i < heaters[0]:
                # house_dict[i] = heaters[0] - i
                min_circle = max(min_circle,heaters[0] - i)
                continue
            if i > heaters[-1]:
                house_dict[i] = i - heaters[-1]
                min_circle = max(min_circle, i - heaters[-1])
                continue
            for j in range(0,len(heaters)):
                if heaters[j] > i:
                    house_dict[i] = min( i - heaters[j-1], heaters[j] - i)
                    min_circle = max(min_circle, house_dict[i])
                    continue
        print(house_dict)
        return min_circle



if __name__ == "__main__":
    a = Solution()
    b = a.findRadius(houses = [1,1,1,1,1,1,999,999,999,999,999], heaters = [499,500,501])
    print(f"final = {b}")