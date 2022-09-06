from re import L


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        hash_map={}
        n = len(s)
        for i, letter in enumerate(s):
            if hash_map.get(letter):
                hash_map[letter].append(i)
            else:
                hash_map[letter] = [i]
        
        l_arr=[None for i in range(n)]
        r_arr=[None for i in range(n)]
        for letter, occur in hash_map.items():
            if len(occur) == 1:
                l_arr[occur[0]] = -1
                r_arr[occur[0]] = n
            else:
                for i, num in enumerate(occur):
                    if i == 0:
                        l_arr[num] = -1
                        r_arr[num] = occur[i+1]
                    elif i == len(occur)-1:
                        l_arr[num] = occur[i-1]
                        r_arr[num] = n
                    else:
                        l_arr[num] = occur[i-1]
                        r_arr[num] = occur[i+1]
        print(l_arr,r_arr)
        res = 0
        for i in range(n):
            res += (i - l_arr[i])*(r_arr[i] - i)
        return res 
        
        

if __name__ == "__main__":
    a = Solution() 
    b = a.uniqueLetterString('leetcode')
    print(b)

# AC