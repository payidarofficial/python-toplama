##############################
# Coded By Pâyidar
##############################

import colorama
from colorama import Fore, Back, Style
colorama.init()

# Soru Cevap
print(Fore.GREEN)
sayi_1 = int(input('1. Sayı Gir: '))
sayi_2 = int(input('2. Sayı Gir: '))

toplam = sayi_1 + sayi_2
print(Fore.WHITE)
print(toplam)
