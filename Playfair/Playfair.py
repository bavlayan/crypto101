# -*- coding: utf-8 -*-

class Playfair:

    def __init__(self):
        # Key is beşiktaş :)
        # Letter checker board - Turkish alphabet
        self.__letters = [["b", "e", "ş", "i", "k"],
                          ["t", "a", "c", "ç", "d"],
                          ["f", "g", "ğ", "h", "ı"],
                          ["j", "l", "m", "n", "o"],
                          ["ö", "p", "r", "s", "u"],
                          ["ü", "v", "y", "z", "x"]
                         ];

        self.__rowCount = len(self.__letters)
        self.__columnCount = len(self.__letters[0])

    def encrypt(self, plain_text):
        plain_text = plain_text.lower()
        blocks = self.__createBlock(plain_text)
        encrypted_text = ""

        for block in blocks:
            first_index = self.__get_indexOfElement(block[0])
            second_index = self.__get_indexOfElement(block[1])
            encrypted_text = encrypted_text + self.__getNewBlock(block, first_index, second_index, False)
        return encrypted_text

    def decrypt(self, cipher_text):
        blocks = self.__createBlock(cipher_text)
        decrypted_text = ""
        for block in blocks:
            first_index = self.__get_indexOfElement(block[0])
            second_index = self.__get_indexOfElement(block[1])
            decrypted_text = decrypted_text + self.__getNewBlock(block, first_index, second_index, True)
        return decrypted_text

    def __getNewBlock(self, current_block, first_index, second_index, isDecrypt):
        index_count = 1
        if isDecrypt:
            index_count = -1

        if first_index[1] is second_index[1]:  # letters of block are same column.
            new_first_index = (first_index[0] + index_count) % self.__rowCount
            new_second_index = (second_index[0] + index_count) % self.__rowCount
            return self.__letters[new_first_index][first_index[1]] + self.__letters[new_second_index][second_index[1]]

        elif first_index[0] is second_index[0]:  # letters of block are same row
            new_first_index = (first_index[1] + index_count) % self.__columnCount
            new_second_index = (second_index[1] + index_count) % self.__columnCount
            return self.__letters[first_index[0]][new_first_index] + self.__letters[second_index[0]][new_second_index]

        else:  # letters of block are neither same row nor same column
            return self.__letters[first_index[0]][second_index[1]] + self.__letters[second_index[0]][first_index[1]]

    def __createBlock(self, current_text):
        blocks = []
        if len(current_text) % 2 is not 0:
            current_text = current_text + "x"

        while(len(current_text) != 0):
            blocks.append(self.__removeDuplicateCharOfBlock(current_text[0:2]))
            current_text = current_text[2:]
        return blocks

    def __removeDuplicateCharOfBlock(self, current_block):
        if current_block[0] is current_block[1]:
            current_block = current_block[:1] + 'x' + current_block[2:]
        return current_block

    def __get_indexOfElement(self, letter):
        for row, k in enumerate(self.__letters):
            for column, l in enumerate(k):
                if letter == l:
                    return row, column
        return -1, -1

