# -*- coding: utf-8 -*-

class Affine:

    def __init__(self, a, b):
        self.__letters = [ "a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k",
                           "l", "m", "n", "o", "ö", "p", "r", "s", "ş", "t", "u", "ü", "v", "y", "z"
                         ]
        self.__a = a
        self.__b = b
        self.__getInverseOfa()

    def __getCipherIndexOfLetter(self, letter):
        if letter in self.__letters:
            index = self.__letters.index(letter)
            cipher_index = (self.__a * index  + self.__b) % len(self.__letters)
            return cipher_index

    def __getPlainIndexOfLetter(self, cipher_letter, inverse_of_a):
        if cipher_letter in self.__letters:
            index = self.__letters.index(cipher_letter)
            plain_index = (inverse_of_a * (index - self.__b)) % len(self.__letters)
            return int(plain_index)

    def encrypt(self, plain_text):
        encrypted_text = ""
        for letter in plain_text:
            cipher_index = self.__getCipherIndexOfLetter(letter)
            if cipher_index is not None:
                encrypted_text = encrypted_text + self.__letters[cipher_index]
            else:
                encrypted_text = encrypted_text + " "
        return encrypted_text

    def decrypt(self, cipher_text):
        decrypted_text = ""
        inverse_of_a = self.__getInverseOfa()
        for letter in cipher_text:
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