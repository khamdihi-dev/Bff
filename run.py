from utama import Bff

import os
try:
     import bs4
except (ModuleNotFoundError,ImportError):
     os.system('pip install bs4')
try:
     import requests
except (ModuleNotFoundError,ImportError):
     os.system('pip install requests')

def main():
    os.system('git pull')
    os.system('clear')
    Bff.false()

if __name__ == '__main__':
   main()
