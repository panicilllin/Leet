def solution(S):
    character_dict = {'B': 0, 'A': 0, 'N': 0}
    for i in S:
        if i in ['B', 'A', 'N']:
            character_dict[i] += 1
    print(character_dict)

    b_times = character_dict['B'] //1
    a_times = character_dict['A'] //3
    n_times = character_dict['N'] //2
    return min(b_times, a_times, n_times)

if __name__ == "__main__":
    a = solution('QABAAAWOBL')
    print(a)
