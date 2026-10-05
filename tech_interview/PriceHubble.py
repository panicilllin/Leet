##
from typing import *


def demo(garden:str, n:int) -> bool:

    for index, value in enumerate(garden):
        print(index, value)

    position=0
    if len(garden) <=2:
        return False if '1' in garden else True
    # print(len(garden))
    for i in range(0, len(garden)):
        # print('----\n',i, garden[i], position)
        if i == 0 and garden[i] == '0' and garden[i+1] =='0':
            position += 1
            garden[i] = 1
            continue

        if i == len(garden)-1 and garden[i] == '0' and garden[i-1] == '0':
            position += 1
            garden[i] = 1
            continue

        if garden[i] == '0' and garden[i-1] == '0' and garden[i+1] =='0':
            position += 1
            garden[i]=1
        print(i, garden[i], position)
    print(position)
    return True if position >= n else False


if __name__ == "__main__":
    res = demo(['1','0', '1', '1'], 1)
    print(res)

