#!/usr/bin/env python
import sys
import os
import re

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

class Twords():
    def __init__(self, dictionary = "words.txt"):
        self.dictionary = dictionary
    def match(self, word, rack):
        W = []
        r = list(rack)
        try:
            for w in list(word):
                W.append(r.pop(r.index(w)))
            return True
        except:
            return False
    def matches(self, rack, required=""):
        rack = str(rack) + str(required)
        matches = []
        with open(os.path.join(__location__, self.dictionary)) as f:
            for w in f.readlines():
                w = w.rstrip()
                if self.match(w, rack):
                    if not required or re.search(required, w):
                        matches.append(w)
        return matches

def main():
    t = Twords()
    for match in t.matches(sys.argv[1]):
        print match

if __name__ == '__main__':
    main()
