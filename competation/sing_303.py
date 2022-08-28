from collections import defaultdict
from typing import List
# from numpy import array
import bisect
# 6124
from sortedcontainers import SortedSet


class Solution1:
    def repeatedCharacter(self, s: str) -> str:
        cha_map = {i:0 for i in 'abcdefghijklmnopqrstuvwxyz'}
        for c in s:
            if cha_map[c] >=1:
                return c
            else:
                cha_map[c] += 1
        return None


# 6125
class Solution2:
    def equalPairs(self, grid: List[List[int]]) -> int:
        grid_t = []
        for i in range(0,len(grid[0])):
            row = []
            for j in range(0,len(grid)):
                row.append(grid[j][i])
            grid_t.append(row)
        print(grid_t)
        res = 0
        for i in grid:
            for j in grid_t:
                if i == j:
                    res += 1
        return res


# 6126
class FoodRatings0:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisine = {}
        self.food_rates = {}
        for i in range(0,len(foods)):
            food = foods[i]
            cui = cuisines[i]
            rate = ratings[i]
            if not self.cuisine.get(cui):
                self.cuisine[cui] = [food]
            else:
                self.cuisine[cui].append(food)
            self.food_rates[food] = rate

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_rates[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        max_rate = -1
        res = None
        for food in self.cuisine[cuisine]:
            if self.food_rates[food] > max_rate:
                res = food
                max_rate = self.food_rates[food]
            elif self.food_rates[food] == max_rate:
                res = min(food, res)
        return res


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_rate = {}
        self.food_cuisine = {}
        self.cuisine_score = defaultdict(SortedSet)

        for i in range(0,len(foods)):
            food = foods[i]
            cui = cuisines[i]
            rate = ratings[i]
            self.food_rate[food] = rate
            self.food_cuisine[food] = cui
            self.cuisine_score[cui].add((-rate, food))
        print(self.cuisine_score)

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_cuisine[food]
        score = self.cuisine_score[cuisine]
        old_rate = self.food_rate[food]
        score.remove((-old_rate,food))
        score.add((-newRating,food))

        self.food_rate[food] = newRating
        print(self.cuisine_score)

    def highestRated(self, cuisine: str) -> str:
        res = self.cuisine_score[cuisine][0][1]
        return res


if __name__ == "__main__":

    a = ["FoodRatings","highestRated","highestRated","changeRating","highestRated","changeRating","highestRated"]
    b = [
        [
            ["kimchi","miso","sushi","moussaka","ramen","bulgogi"],
            ["korean","japanese","japanese","greek","japanese","korean"],
            [9,12,8,15,14,7]
        ],
        ["korean"],
        ["japanese"],
        ["sushi",16],
        ["japanese"],
        ["ramen",16],
        ["japanese"]
    ]

    c = FoodRatings(b[0][0],b[0][1],b[0][2])
    for i in range(1,len(a)):
        if a[i]=='highestRated':
            print(c.highestRated(b[i][0]))
        elif a[i] == 'changeRating':
            c.changeRating(b[i][0],b[i][1])

