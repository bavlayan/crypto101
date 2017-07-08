# -*- coding: utf-8 -*-

class Caesar:

    def __init__(self, key):        
        #Turkish alphabet
        self.__letters = [ "a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", 
                           "l", "m", "n", "o", "ö", "p", "r", "s", "ş", "t", "u", "ü", "v", "y", "z"]
        
        self.__key = key

    def encrypt(self, plain_text):
        self.__key = abs(self.__key)
        return self.__run_caesar_algorithm(plain_text)
    
    def decrypt(self, chiper_text):
        self.__key = -self.__key
        return self.__run_caesar_algorithm(chiper_text)

    def __run_caesar_algorithm(self, m_text):
        m_text = m_text.lower()
        new_text = ""
        for character in m_text:
            index = self.__get_indexOfLetter(character)
            if index is not None:
                new_text = new_text + self.__get_encrypte_letter(index)
            else:
                new_text = new_text + character
        return new_text


    def __get_indexOfLetter(self, character):
        for index, letter in enumerate(self.__letters):
            if letter == character:
                return index
        return None

    def __get_encrypte_letter(self, index):
        new_index = index + self.__key
        if new_index > (len(self.__letters) - 1) or new_index < 0:
            new_index = new_index % len(self.__letters)
        return self.__letters[new_index]