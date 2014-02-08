import unittest
from expecter import expect
from twords import Twords

class TestTwords(unittest.TestCase):
    def test_words_can_be_matched_by_tiles(self):
        t = Twords()
        expect(t.match("pies", "eips")) == True
    def test_words_that_cant_be_matched_by_tiles(self):
        t = Twords()
        expect(t.match("spies", "eips")) == False
    def test_words_can_be_matched_by_only_some_tiles(self):
        t = Twords()
        expect(t.match("pi", "eips")) == True
    def test_the_default_dictionary(self):
        t = Twords()
        expect(t.dictionary) == "words.txt"
    def test_a_specified_dictionary(self):
        t = Twords("./test/test_words.txt")
        expect(t.dictionary) == "./test/test_words.txt"
    def test_matches(self):
        t = Twords("./test/test_words.txt")
        expect(t.matches("eips")) == ["is"]
    def test_matches_accept_required_tiles(self):
        t = Twords("./test/test_words.txt")
        expect(t.matches("eps", "i")) == ["is"]


