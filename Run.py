import os
import datetime
import time
from builtins import *

builtglob = list(globals().keys())

from binascii import hexlify
from tokenize import tokenize, untokenize, TokenInfo
from io import BytesIO
from re import findall
from random import choice, shuffle, randint
from zlib import compress

class Quantum:

    def __init__(self, content: str, clean=True, obfcontent=True, renlibs=True, renvars=True, addbuiltins=True, randlines=True, shell=True, camouflate=True, safemode=True, ultrasafemode=False) -> None:
        self.content = content
        self.clean = clean
        self.obfcontent = obfcontent
        self.renlibs = renlibs
        self.renvars = renvars
        self.addbuiltins = addbuiltins
        self.randlines = randlines
        self.shell = shell
        self.camouflate = camouflate
        self.safemode = safemode
        self.ultrasafemode = ultrasafemode
        self.obfuscated_content = ""

    def encrypt_file(self, filename):
        with open(filename, 'r') as file:
            content = file.read()

        self.content = content
        self._obfuscate()
        self._write_obfuscated_file(filename)

    def _obfuscate(self):
        self._apply_comments()
        self._apply_headers()
        self._apply_obfuscation()

    def _apply_comments(self):
        self.content = fr"""
# This Code Has Been Obfuscated By Ferly Afriliyan

# {datetime.datetime.now().strftime("%d %B %Y")}

__Quantum__ = "Obfuscated Code by Ferly Afriliyan"
__File__    = "Quantum__Obfuscated__"

# 

__Author__  = "[ Ferly Afriliyan (Avs4x-Dvanmeploph) ]"
__Github__  = "https://github.com/FerlyXyn/Quantum"
__License__ = "EPL-2.0"

# 

__Facebook__  = "www.facebook.com/freya.xyn"
__Instagram__ = "Instagram.com/afriliyanferlly_shishigami"


{self.content.strip()}"""

    def _apply_headers(self):
        self.content = self.content.replace("#!python", "#!Quantum__Obfuscated__")
        self.content = self.content.replace("# -*- coding: utf-8 -*-", "# -*- coding: Quantum__Obfuscated__ -*-")

    def _apply_obfuscation(self):
        # Terapkan teknik obfuskasi di sini
        pass

    def _write_obfuscated_file(self, filename):
        obfuscated_filename = f"Quantum_{os.path.splitext(filename)[0]}.py"
        with open(obfuscated_filename, 'w') as file:
            file.write(self.content)

        print(f"File {filename} berhasil dienkripsi. File hasil enkripsi tersimpan dalam {obfuscated_filename}.")

# Fungsi utama
def main():
    os.system("mode con: cols=150 lines=47")
    os.system("title Quantum")
    os.system("cls")
    print()

    file = input("Drag the file you want to obfuscate -> ")
    print()

    try:
        with open(file, mode='rb') as f:
            script = f.read().decode('utf-8')
        filename = os.path.basename(file)
    except:
        input("Invalid file!")
        exit()

    skiprenaming = input("Skip the renaming of libraries and variables [y/n] -> ") == 'y'
    print()
    skipchunks = input("Skip the protection of chunks [y/n] -> ") == 'y'

    renvars, renlibs = (False, False) if skiprenaming else (True, True)
    randlines, shell = (False, False) if skipchunks else (True, True)

    print()

    Quan = Quantum(content=script, renvars=renvars, renlibs=renlibs, randlines=randlines, shell=shell)
    script = Quan.content

    now = time.time()
    Quan.encrypt_file(filename)
    now = round(time.time() - now, 2)

    print()
    input(f"Obfuscation completed successfully in {now}s.")

if __name__ == '__main__':
    main()
