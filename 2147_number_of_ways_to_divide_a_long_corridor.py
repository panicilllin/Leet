class Solution:
    def numberOfWays0(self, corridor: str) -> int:
        first_s = 0
        last_s = len(corridor)

        for i in range(0, len(corridor)):
            first_s = i
            if corridor[i] == 'S':
                break
            
        for i in range (len(corridor)-1, first_s-1, -1):
            last_s = i
            if corridor[i] == 'S':
                break
        print(first_s, last_s)
        if first_s >= last_s:
            return 0

        ans = 0
        seat_num = 0
        seat_before = None
        for i in range(first_s, last_s+1):
            # print(i, corridor[i])
            if corridor[i] == 'P' and seat_num%2 == 0:
                ans += 1
                print(i, corridor[i],seat_num, ans)
            elif corridor[i] == 'S':
                seat_num += 1
                if seat_before == i-1:
                    seat_before = i
                    continue
                if i == last_s:
                    break
                if seat_num%2 == 0:
                    ans += 1
                    seat_before = i
                    print(i, corridor[i],seat_num, ans)
                    

        print(seat_num)
        if seat_num%2 == 1:
            return 0
        if seat_num == 2:
            return 1
        return ans % (10**9 + 7)

    def numberOfWays(self, corridor: str) -> int:
        seatsToLeft = 0        
        consecutivePlants = 0
        ans = 1
            
        for c in corridor:
            if c == "P":
                if seatsToLeft and seatsToLeft % 2 == 0:
                    consecutivePlants += 1
            else:
                seatsToLeft += 1
            
                if seatsToLeft % 2 == 1 and consecutivePlants != 0:
                    ans *= (consecutivePlants+1)
                    consecutivePlants = 0
                
        return ans%(10**9+7) if (seatsToLeft and seatsToLeft%2 == 0) else 0


if __name__ == "__main__":
    a = Solution()
    b = a.numberOfWays("SSPSSPSSSPPSPSPPS")
    print(b)