# An encryption class dedicated to Compensa SOAP services.
# Written by: Aurimas Navickas ( aurimas.navickas@gmail.com )

# -*- coding: utf-8 -*-

import base64
import binascii
import datetime
from Crypto.Cipher import AES


class CompensaEncryption:
    ENCRYPTION_KEY = b'82d6079a253b701e4da0f2c72efeca6a'
    BLOCK_SIZE = 16
    PADDING = u'\u0000'
    cipher = None

    def __init__(self, init_cipher=False, encryption_key=None, block_size=None, padding=None):
        self.ENCRYPTION_KEY = encryption_key if encryption_key else self.ENCRYPTION_KEY
        self.ENCRYPTION_KEY = binascii.unhexlify(self.ENCRYPTION_KEY)
        self.BLOCK_SIZE = block_size if block_size else self.BLOCK_SIZE
        self.PADDING = padding if padding else self.PADDING

        if init_cipher:
            self._init_cipher()

    def _init_cipher(self, mode='AES.MODE_ECB', iv=None):
        if iv is None:
            iv = '\00' * self.BLOCK_SIZE
        mode = eval(mode) if int(eval(mode)) else AES.MODE_ECB
        self.cipher = AES.new(self.ENCRYPTION_KEY, mode, iv)

    def _add_padding(self, text=''):
        pad_string = self.PADDING * ((self.BLOCK_SIZE - len(text)) % self.BLOCK_SIZE)
        return ''.join([text, pad_string])

    def _strip_padding_old(self, text=''):
        return str(text).rstrip(self.PADDING)

    def _strip_padding(self, text=''):
        return str(text)[21:].strip()

    def encrypt(self, text=''):
        raw_text = self._add_padding(self._get_datetime_str() + text)

        if self.cipher is None:
            self._init_cipher()

        return base64.b64encode(self.cipher.encrypt(raw_text))

    def decrypt(self, encrypted_text):
        if self.cipher is None:
            self._init_cipher()

        try:
            encoded = base64.b64decode(encrypted_text)
            return self._strip_padding(self.cipher.decrypt(encoded))
        except:
            print('Decryption Error!')
            return None

    @staticmethod
    def _get_datetime_str():
        date = datetime.datetime.now()
        return '00.' + date.strftime("%S:%M:%H%d-%m-%Y")
