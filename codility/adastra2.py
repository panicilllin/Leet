

def f(a):
    if a > 0:
        b = a + f(a//2)
        return b
    else:
        return 0


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S):
    # Implement your solution here
    alpha = {i: 0 for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    position = {i: [] for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    for idx, word in enumerate(S):
        alpha[word] += 1
        position[word].append(idx)
    # print(alpha)
    alpha = {k: v for k, v in alpha.items() if v != 0}
    print(alpha)

    keep_list = []
    for word, times in alpha.items():
        if times % 2 != 0:
            keep_list.append(word)
    position = {k: v for k, v in position.items() if k in keep_list}
    keep_list.sort()
    print(keep_list)
    ans = ''
    keep_position = {i: None for i in keep_list}
    last_p = None
    for w in keep_list:
        keep_position[w] = bubble(keep_position, keep_position[w])
    # for w in keep_list:
    #     if not last_p:
    #         last_p = position[w][0]
    #         keep_position[w] = last_p
    #         continue
    #     if position[w][0] > last_p:
    #         last_p = position[w][0]
    #         keep_position[w] = last_p
    #         continue
    #     if position[w][-1] < last_p:
    #         keep_position[w] = position[w][-1]
    #         continue
    #     for p in position[w]:
    #         if p > last_p:
    #             last_p = p
    #             keep_position[w] = last_p
    #             break
    print(keep_position)
    ans_list = [k for k, v in sorted(keep_position.items(), key=lambda item: item[1])]
    ans = ''
    for w in ans_list:
        ans += w

    return ans


def bubble(keep_position: list, position: list):
    # keep_position = [v for v in keep_position.values()]
    if position[0] > keep_position[-1]:
        return position[0]
    for i in position[-1:0:-1]:

    n = len(keep_position)
    for last_p in keep_position[n: 0: -1]:
        for p in position:
            if p > last_p:
                return p






# # define a function to check if a string is a palindrome
# def is_palindrome(s):
#     # reverse the string and compare it with the original
#     return s == s[::-1]
#
# # define a function to find the longest palindrome in a string
# def longest_palindrome(s):
#     # initialize the longest palindrome as an empty string
#     longest = ""
#     # loop through all possible substrings of s
#     for i in range(len(s)):
#         for j in range(i + 1, len(s) + 1):
#             # get the substring from i to j
#             substring = s[i:j]
#             # check if the substring is a palindrome and longer than the current longest
#             if is_palindrome(substring) and len(substring) > len(longest):
#                 # update the longest palindrome
#                 longest = substring
#     # return the longest palindrome
#     return longest
#
# # test the function with some examples
# print(longest_palindrome("abaxyzzyxf")) # output: xyzzyx
# print(longest_palindrome("racecar")) # output: racecar
# print(longest_palindrome("forgeeksskeegfor")) # output: geeksskeeg


if __name__ == "__main__":
    a = solution('AKFKFMOGKFB')
    print(a)