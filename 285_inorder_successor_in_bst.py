from operator import mod


class Solution:
    def __init__(self):
        self.prime = []
        for i in range(1,101):
            ist_prime=True
            for j in range(2,i):
                if (i%j) ==0:
                    # print(f"{i} not prime")
                    ist_prime=False
                    break
            if ist_prime:
                # print(f"{i} ist prime")
                self.prime.append(i)
        del self.prime[0]
        # print(self.prime,len(self.prime))

    def numPrimeArrangements(self, n: int) -> int:
        mod = pow(10,9) + 7
        # print(f"mod={mod}")
        prime_num=0
        for i in range(1,n+1):
            if i in self.prime:
                prime_num += 1
        res=1
        # print(f"prn={prime_num}")
        for i in range(prime_num,1,-1):
            # print(f"i=={i}")
            res = res*i % mod
        for i in range(n-prime_num,1,-1):
            # print(f"i=={i}")
            res = res * i % mod
        # print(prime_num)
        return res



if __name__ == "__main__":
    a = Solution()
    b = a.numPrimeArrangements(100)
    print(b)



