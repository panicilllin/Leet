

def rand_words(n):
    import random, string
    return ''.join(random.choice(string.ascii_lowercase + '_') for _ in range(n))


class SearchByHash:
    def __init__(self, words: list) -> None:
        """
        initial of this class, input a word list
        :param words: word list
        :return: None
        """
        self.words = words

    @staticmethod
    def gen_fingerprint(_word: str) -> str:
        """
        generate a string, store the count of each letter
        O(n)
        for example, if input is aabc, output should be '2.1.1.0.0.···.0.'
        :param _word: word string
        :return: hash string of input word string
        """
        alphabet = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        alphabet['_'] = 0

        for letter in _word.lower():
            # in case other char in word
            if letter not in alphabet.keys():
                continue
            alphabet[letter] += 1
        _res = ''
        # second loop, travel through each letter of word
        for val in alphabet.values():
            _res += str(val)
            _res += '.'
        # print(f"wrod={_word}, hash={_res}")
        return _res

    def find(self, target_word: str):
        """
        find word from list whic has the same character composition and occur time with target word
        generate hash values for each word and compare them
        time: O(n^2)
        space: O(1)
        :param target_word: target word been looking for
        :return: list of words similar to the target word
        """
        if not self.words:
            return []
        target_length = len(target_word)
        target_fingerprint = self.gen_fingerprint(target_word)
        res = []
        # first loop, travel through words
        for word in self.words:
            # filter by length
            if len(word) != target_length:
                continue
            if type(word) != str:
                continue
            word_fingerprint = self.gen_fingerprint(word)
            if word_fingerprint == target_fingerprint:
                res.append(word)
        return res


class SearchBySort(SearchByHash):

    def __init__(self, words: list) -> None:
        """
        initial of this class, input a word list
        :param words: word list
        :return: None
        """
        super().__init__(words)

    @staticmethod
    def sort_word(_word: str) -> str:
        """
        sort given string word and return
        time: O(n log n)
        space: O(n)
        :param _word: word string
        :return: sorted word string
        """
        return ''.join(sorted(_word.lower()))

    def find(self, target_word: str) -> list:
        """
        find word from list whic has the same character composition and occur time with target word
        Using sort to compare two letter.
        would be benefit for time complexity,
        but space complexity would be large depend on the length of each word.
        time: O(nlogn)
        space: O(n)
        :param target_word: target word been looking for
        :return: list of words similar to the target word
        """

        if not self.words:
            return []

        target_sorted = self.sort_word(target_word)
        target_length = len(target_word)
        res = []

        for word in self.words:
            # filter by length
            if len(word) != target_length:
                continue
            if type(word) != str:
                continue

            if self.sort_word(word) == target_sorted:
                res.append(word)
        return res


if __name__ == "__main__":
    cls_hash = SearchByHash(["helloworld", "foo", "bar", "stylight_team", "seo", "oose", "eso"])
    cls_sort = SearchByHash(["helloworld", "foo", "bar", "stylight_team", "seo", "oose", "eso"])
    demo1 = cls_hash.find("eos")
    print(demo1)
    demo2 = cls_sort.find("eos")
    print(demo2)
