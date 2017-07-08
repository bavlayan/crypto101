# -*- coding: utf-8 -*-

class Vigenere:

    def __init__(self, key_word):
        # Turkish alphabet
        self.__letters = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k",
                          "l", "m", "n", "o", "ö", "p", "r", "s", "ş", "t", "u", "ü", "v", "y", "z"]
        self.__key_word = key_word
        self.__key_index = []

    def encrypt(self, plain_text):
        encrypted_text = ""
        self.__key_index = self.__getKeyIndex(plain_text)
        count = 0
        for letter in (plain_text):
            if letter in self.__letters:
                new_index = (self.__getIndexOfLetter(letter) + self.__key_index[count]) % len(self.__letters)
                encrypted_text = encrypted_text + self.__letters[new_index]
                count = count + 1
            else:
                encrypted_text = encrypted_text + " "
        return encrypted_text

    def decrypt(self, chiper_text):
        decrypted_text = ""
        count = 0
        for letter in (chiper_text):
            if letter in self.__letters:
                new_index = (self.__getIndexOfLetter(letter) - self.__key_index[count]) % len(self.__letters)
                decrypted_text = decrypted_text + self.__letters[new_index]
                count = count + 1
            else:
                decrypted_text = decrypted_text + " "
        return decrypted_text

    def __getIndexOfLetter(self, letter):
        if letter in self.__letters:
            return self.__letters.index(letter)

    def __getKeyIndex(self, plain_text):
        key_index = []
        count = 0
        for i in range(len(plain_text)):
            if i % len(self.__key_word) == 0:
                count = 0
            key_index.append(self.__getIndexOfLetter(self.__key_word[count]))
            count = count + 1
        return key_index