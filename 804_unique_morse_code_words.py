class Solution:
    alphamap = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
                ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # idx = ord('w')-ord('a')
        morses=[]
        for word in words:
            morse=''
            for letter in word:
                morse+=self.alphamap[ord(letter)-ord('a')]
            # print(word, morse)
            if morse not in morses:
                morses.append(morse)
        return len(morses)
