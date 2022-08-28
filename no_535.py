import string
import random


class Codec:
    def __init__(self):
        self.origin_to_tiny = {}
        self.tiny_to_origin = {}
        self.k = 6
        self.ss = string.ascii_letters + string.digits

    def encode(self, longUrl: str) -> str:
        while longUrl not in self.origin_to_tiny.keys():
            cur = ''.join([self.ss[random.randint(0, len(self.ss) - 1)] for _ in range(self.k)])
            if cur in self.tiny_to_origin.keys():
                continue
            self.tiny_to_origin[cur] = longUrl
            self.origin_to_tiny[longUrl] = cur
        return self.origin_to_tiny[longUrl]

    def decode(self, shortUrl: str) -> str:
        return self.tiny_to_origin[shortUrl]
