#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__  = 'Batuhan AVLAYAN - b.avlayan@gmail.com'
__version__ = '1.0'

from Polybius.Polybius import Polybius
from Caesar.Caesar import Caesar
from Affine.Affine import Affine

if __name__ == "__main__":

    message = "batuhan avlayan"
    print("Original text: %s " % (message))

    m_polybius = Polybius()
    encrypted_text = m_polybius.encrypt(message)
    print("Encrypted text (Polybius): %s " % (encrypted_text))
    
    decrypted_text = m_polybius.decrypt(encrypted_text)
    print("Decrypted text (Polybius): %s " % (decrypted_text))

    m_key = 5
    m_caesar = Caesar(m_key)
    encrypted_text = m_caesar.encrypt(message)
    print("Encrypted text (Caesar - key: %d): %s " % (m_key, encrypted_text))

    decrypted_text = m_caesar.decrypt(encrypted_text)
    print("Decrypted text (Caesar - key: %d): %s " % (m_key, decrypted_text))

    m_a = 8
    m_b = 2
    m_affine = Affine(m_a, m_b)
    encrypted_text = m_affine.encrypt(message)
    print("Encrypted text (Affine: y=%dx + %d): %s " % (m_a, m_b, encrypted_text))

    decrypted_text = m_affine.decrypt(encrypted_text)
    print("Decrypted text (Affine: y=%dx + %d): %s " % (m_a, m_b, decrypted_text))