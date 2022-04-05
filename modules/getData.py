import requests
import sys
import json
from colorama import Fore, Back, Style
import os

def getGeo(syA1):
    r = requests.get('http://ip-api.com/json/'+syA1)
    response = json.loads(r.text)

    #Filtrer og skriv ut (data for spesifikke felt)
    print ( "\n" + Fore.YELLOW + "[*] Kjører Geo-lokasjon sjekk mot "+ " " + sys.argv[1] + "\n")
    print ( Fore.WHITE + "Land: "+ response["country"])
    print ( "Region: " + response["regionName"])
    print ( "By: " + response["city"])
    print ( "Leverandør: "+response["org"])
    print ( "Lengdegrad: ", response["lon"])
    print ( "Breddegrad: ", response["lat"])
    print ( "ISP: "+ response["isp"] + "\n") 
    print ( Fore.GREEN + "[*] IP Søk Fullført!cd Programmering" + "\n")