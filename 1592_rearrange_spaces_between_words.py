class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = []
        blank = 0
        last_word=''
        for character in text:
            if character == ' ':
                blank += 1
                if last_word != '':
                    words.append(last_word)
                    last_word = ''
            else:
                last_word += character
        if last_word != '':
            words.append(last_word)
        print(blank, words)
        if len(words) == 1:
            gap = 0
            tail = blank
        else:
            gap = blank // (len(words)-1)
            tail = blank % (len(words)-1)
        res = ''
        for word in words[:-1]:
            res += word + ' '*gap
        res += words[-1] + ' '*tail
        return res
# AC