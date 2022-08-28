class Solution:
    def countDigitOne(self, n: int) -> int:
        n_str = str(n)
        n_list = list(str(n))
        n_len = len(n_str)
        res = 0
        if n == 0:
            return 0
        if n_len == 1:
            return 1
        for i in range(0, n_len):
            print(f"res={res, i}")
            if i == 0:
                if n_str[i] == '1':
                    # print(f"n_str[i+1:]={n_str[i + 1:]}")
                    res += int(n_str[i + 1:]) + 1
                else:
                    res += pow(10, (n_len - 1 - i))
                # print(10 ^ (n_len - 1 - i), int(n_str[i + 1:]))

                continue
            print(f"n_str[:i]={n_str[:i]},(n_len - i)={(n_len - i)}")
            res += int(n_str[:i]) * pow(10, (n_len - 1 - i))
            print(f"res2={res}")
            if n_str[i] == '0':
                continue
            elif n_str[i] == '1':
                if i == n_len - 1:
                    res += 1
                else:
                    res += int(n_str[i + 1:]) + 1
                # print(f"res3={res}")
            else:
                res += pow(10, (n_len - 1 - i))
        print(f"res4={res}")
        return res


if __name__ == "__main__":
    a = Solution()
    b = a.countDigitOne(n=100)
    print(b)
