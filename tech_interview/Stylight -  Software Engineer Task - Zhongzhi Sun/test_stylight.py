import stylight as sl


def test_find_hash():
    big_target = sl.rand_words(10000)
    test_cases = [
        [["helloworld", "foo", "bar", "stylight_team", "seo", "oose", "eso"], "eos", ['seo', 'eso']],
        [["@@@", '001', "alice", "cliae", "abc", "bac", "cab"], "aceil", ["alice", "cliae"]],
        [[], "hello", []],
        [[[big_target]+[sl.rand_words(10000)] * 10000, big_target, [big_target]], big_target, [big_target]]
    ]
    for test_case in test_cases:
        cls = sl.SearchByHash(test_case[0])
        res = cls.find(test_case[1])
        assert res == test_case[2]


def test_find_sort():
    big_target = sl.rand_words(10000)
    test_cases = [
        [["helloworld", "foo", "bar", "stylight_team", "seo", "oose", "eso"], "eos", ['seo', 'eso']],
        [["@@@", '001', "alice", "cliae", "abc", "bac", "cab"], "aceil", ["alice", "cliae"]],
        [[], "hello", []],
        [[[big_target]+[sl.rand_words(10000)] * 10000, big_target, [big_target]], big_target, [big_target]]
    ]
    for test_case in test_cases:
        cls = sl.SearchBySort(test_case[0])
        res = cls.find(test_case[1])
        assert res == test_case[2]


if __name__ == '__main__':
    pass
