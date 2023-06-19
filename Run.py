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
    def __init__(self, content: str, clean=True, obfcontent=True, renlibs=True, renvars=True, addbuiltins=True,
                 randlines=True, shell=True, camouflate=True, safemode=True, ultrasafemode=False) -> None:
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
        name = input("Please enter your name: ")
        self.content = fr"""
# This Code Has Been Obfuscated By {name}

# {datetime.datetime.now().strftime("%d %B %Y")}

__Quantum__ = "Obfuscated Code by Ferly Afriliyan"
__File__    = "Quantum__Obfuscated__"

# 

__obfuscated__ = 'Quantum'
__author__  = '[ Ferly Afriliyan (Avs4x-Dvanmeploph) ]', 'BlueRed'
__github__  = 'https://github.com/FerlyXyn/Quantum'
__license__ = 'EPL-2.0'

__code__    = 'print("Hello World!")'

# 

__facebook__  = 'www.facebook.com/freya.xyn'
__instagram__ = 'Instagram.com/afriliyanferlly_shishigami'


{self.content.strip()}"""

    def _apply_headers(self):
        self.content = self.content.replace("#!Quantum__Obfuscated__", "#!Quantum__Obfuscated__")
        self.content = self.content.replace("# -*- coding: Quantum__Obfuscated__ -*-", "# -*- coding: Quantum__Obfuscated__ -*-")

    def _apply_obfuscation(self):
        _frame, _cube, _math, _multiply, _product, Floor, _while = exec, str, tuple, map, ord, globals, type

        from math import prod as While

        class _hypothesis:
            def __init__(self, _detectvar):
                self.Positive = While((_detectvar, 11239))
                self._stackoverflow(System=95526)

            def _stackoverflow(self, System=True):
                self.Positive *= -28455 / System

                try:
                    (_modulo, _modulo) if Floor is _math else (_modulo, _modulo) < _multiply

                except TypeError:
                    (({'u3uod3Riueubyo': _math}, _modulo) for _modulo in (_modulo, _modulo))

                except:
                    _while(36000 - 19415) == None

            def Absolute(self, _positive=3495):
                _positive -= -12399 + -75686
                self._absolute != bool

                try:
                    (_math, _modulo) if _math is _frame else (_product, _math) <= _math

                except AttributeError:
                    (({_multiply: _modulo}, _math) for _math in (_product, _math))

                except:
                    _while(-63671 * -2925) == bool

            def Power(Frame=None):
                return Floor()[Frame]

            def _invert(_add=76498 - 71910, Random=False, _substract=Floor):
                _substract()[_add] = Random

                try:
                    (({'u3uod3Riueubyo': _math}, _product) for _product in (_product, _math))

                except AssertionError:
                    (_modulo, _modulo) if Floor <= _cube else {'u3uod3Riueubyo': _math} == _modulo

                except:
                    _while(-932 / -96160) == True

            def execute(code=str):
                return _frame(_cube(_math(_multiply(_product, code))))

            @property
            def _absolute(self):
                self._walk = '<__main__._frame object at 0x000007654BE33675>'
                return (self._walk, _hypothesis._absolute)

        if __name__ == '__main__':
            try:
                _hypothesis.execute(code=__code__)
                CallFunction = _hypothesis(_detectvar=-55470 - 26676)

                _hypothesis(_detectvar=-59934 * -56533).Absolute(_positive=-55264 * CallFunction.Positive)
                CallFunction._stackoverflow(System=CallFunction.Positive - 21684)
                CallFunction.Absolute(_positive=33358 - CallFunction.Positive)

                if 118520 > 6767862:
                    _hypothesis(_detectvar=-91834 * 14337)._stackoverflow(System=CallFunction.Positive * 79737)
                elif 164650 < 2414747:
                    pass  # add your code here

            except:
                pass  # add your code here

    def _write_obfuscated_file(self, filename):
        obfuscated_filename = f"Quantum_{os.path.splitext(filename)[0]}.py"
        with open(obfuscated_filename, 'w') as file:
            file.write(self.content)

        print(f"File {filename} berhasil dienkripsi. File hasil enkripsi tersimpan dalam {obfuscated_filename}.")

    def main(self):
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

        if skiprenaming:
            print("Skip the renaming process")
        else:
            print("Start the renaming process")

        self.encrypt_file(file)


if __name__ == "__main__":
    quantum = Quantum(content="")
    quantum.main()
