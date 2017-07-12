#coding:utf8

class Polybius:

    def __init__(self):
        #Letter checker board - Turkish alphabet
        self.__letters = [["a", "b", "c", "ç"],
                          ["d", "e", "f", "g"],
                          ["ğ", "h", "ý", "i"],
                          ["j", "k", "l", "m"],
                          ["n", "o", "ö", "p"],
                          ["r", "s", "ş", "t"],
                          ["u", "ü", "v", "y", "z"]
                         ];

    def encrypt(self, plain_text):
        encrypted_text = ""
        plain_text = plain_text.lower()
        for character in plain_text:
            row, column = self.__get_indexOfElement(character)
            if row == -1 and column == -1:
                encrypted_text = encrypted_text + " "
            else:
                encrypted_text = encrypted_text + str(row) + str(column)
        return encrypted_text

    def decrypt(self, cipher_text):
        decrypted_text = ""
        cipher_message = cipher_text.split(" ")
        for cipher_word in cipher_message:
            for i in range(0, len(cipher_word) - 1, 2):
                decrypted_text = decrypted_text + self.__get_letterByIndex(cipher_word[i:i+2])
            decrypted_text = decrypted_text + " "
        return decrypted_text

    def __get_indexOfElement(self, letter):
        for row, k in enumerate(self.__letters):
            for column, l in enumerate(k):
                if letter == l:
                    return row, column
        return -1, -1

    def __get_letterByIndex(self, index):
        row = index[0]
        column = index[1]
        return self.__letters[int(row)][int(column)]