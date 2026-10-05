class Solution:
    def dayOfYear(self, date: str) -> int:
        normal_month=[0,31,59,90,120,151,181,212,243,273,304,334]
        rain_month = [0,31,60,91,121,152,182,213,244,274,305,335]
        year,month,day = map(int, date.split('-'))
        month_dict = rain_month if (year%4 == 0 and year%100 != 0) or year%400==0 else normal_month
        day_in_year = month_dict[month-1] + day
        return day_in_year

if __name__ == "__main__":
    a = Solution()
    b = a.dayOfYear(date = "2019-02-10")
    print(f"final = {b}")