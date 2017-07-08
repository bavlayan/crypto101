# -*- coding: utf-8 -*-

class Affine:

    def __init__(self, a, b):
        self.__letters = [ "a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k",
                           "l", "m", "n", "o", "ö", "p", "r", "s", "ş", "t", "u", "ü", "v", "y", "z"
                         ]
        self.__a = a
        self.__b = b
        self.__getInverseOfa()

    def __getChiperIndexOfLetter(self, letter):
        if letter in self.__letters:
            index = self.__letters.index(letter)
            chiper_index = (self.__a * index  + self.__b) % len(self.__letters)
            return chiper_index

    def __getPlainIndexOfLetter(self, chiper_letter, inverse_of_a):
        if chiper_letter in self.__letters:
            index = self.__letters.index(chiper_letter)
            plain_index = (inverse_of_a * (index - self.__b)) % len(self.__letters)
            return int(plain_index)

    def encrypt(self, plain_text):
        encrypted_text = ""
        for letter in plain_text:
            chiper_index = self.__getChiperIndexOfLetter(letter)
            if chiper_index is not None:
                encrypted_text = encrypted_text + self.__letters[chiper_index]
            else:
                encrypted_text = encrypted_text + " "
        return encrypted_text

    def decrypt(self, chiper_text):
        decrypted_text = ""
        inverse_of_a = self.__getInverseOfa()
        for letter in chiper_text:
            plain_index = self.__getPlainIndexOfLetter(letter, inverse_of_a)
            if plain_index is not None:
                decrypted_text = decrypted_text + self.__letters[plain_index]
            else:
                decrypted_text = decrypted_text + " "
        return decrypted_text

    def __getInverseOfa(self):
        for i in range(len(self.__letters)):
            if self.__a * i % len(self.__letters) == 1:
                return i