# -*- coding: utf-8 -*-

class Vigenere:

    def __init__(self, key_word):
        # Turkish alphabet
        self.__letters = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k",
                          "l", "m", "n", "o", "ö", "p", "r", "s", "ş", "t", "u", "ü", "v", "y", "z"]
        self.__key_word = key_word