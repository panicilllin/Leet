def MinWindowSubstring(strArr):
    # print(strArr)
    # code goes here
    N = strArr[0]
    K = strArr[1]
    alpha_dict = {}
    for i in K:
        if not alpha_dict.get(i):
            alpha_dict[i]=0
        alpha_dict[i] +=1
    # print(alpha_dict)

    def guess_right(i,parstr):
        while i < len(parstr):
            substr = parstr[:i]
            flg=True
            for key,val  in alpha_dict.items():
                if substr.count(key) < val:
                    flg = False
                    break
            if flg:
                return i
            i+=1
        return len(parstr)
                    
    
    def guess_left(i,parstr):
        while i < len(parstr):
            substr = parstr[i:]
            for key,val  in alpha_dict.items():
                if substr.count(key) < val:
                    return i-1
            i+=1
    right = guess_right(len(K),N)
    left = guess_left(0,N[:right])
    # print(left,right)
    return N[left:right]


# keep this function call here 
# print(MinWindowSubstring(input()))

if __name__ == '__main__':
    a = MinWindowSubstring(["ahffaksfajeeubsne", "jefaa"])
    print(a)