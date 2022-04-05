import requests
import sys
import json
from colorama import Fore, Back, Style
import os

def command(syA2, syA1):
   print("##################################### \n")
   if syA2 == '--nmap' or syA2 == '-n':
      print('--------------------------   -------------------------------------------')
      print("Hvis Nmap reagerer tregt, vennligst vent, noen ganger tar det litt tid.")
      print('--------------------------------------------------------------------- \n \n')
      ip = syA1
      nmapcc = os.system('nmap ' + ip)
      print(nmapcc)
      sys.exit(0)

   else:
      print('Se gjennom kommandoen etter IP, \nwrite python ipinfoNO.py --command eller -c for å se tilgjengelige kommandoer')
   print("\n##################################### \n")

def listCommand():
      print(Fore.WHITE+'# Commands')
      print('python ipinfoNO.py --help eller -h                   (Vis hjelp)')
      print('python ipinfoNO.py 138.121.128.19 --nmap eller -n    (Nmap standard)')
      print('python ipinfoNO.py 138.121.128.19                    (Standard, info om IP)')
      print('python ipinfoNO.py --commands eller -c               (Vis tilgjengelige kommandoer )')
