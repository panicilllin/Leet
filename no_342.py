class Solution:
    n_list = [1]
    for i in range(20):
        n_list.append(n_list[-1] * 4)

    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True

        n_list = [1]
        for i in range(20):
            n_list.append(n_list[-1] * 4)
        if n in self.n_list:
            return True
        return False