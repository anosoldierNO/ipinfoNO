import requests
import sys
import json
from colorama import Fore, Back, Style
import os

def check(syA1):
    print ( "\n" + Fore.YELLOW + "[*] Kjører omdømmesjekk mot"+ " ", syA1 + "\n")

    url = 'https://api.abuseipdb.com/api/v2/check'

    querystring = {
        'ipAddress': syA1,
        'maxAgeInDays': '90'
    }

    headers = {
        'Accept': 'application/json',
        'Key': '58878ed65228db88eddfda4983bce5d19d425ddf81f427857b3f59f11aecc34f127862a1cc7d4581'
    }

    response = requests.request(method='GET', url=url, headers=headers, params=querystring)
 
    # Formatted output
    decodedResponse = json.loads(response.text)
    print ( Fore.WHITE + "Domain: " + json.dumps(decodedResponse ["data"]["domain"]))
    print ( "Hostnavn: " + json.dumps(decodedResponse ["data"]["hostnames"]))
    print ( "Type: " + json.dumps(decodedResponse ["data"]["usageType"]))
    print ( "Tillit til misbruk: " + json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]))
    print ( "Antall rapporterte ganger: " + json.dumps(decodedResponse ["data"]["totalReports"]))
    print ( "Sist rapportert " + json.dumps(decodedResponse ["data"]["lastReportedAt"]))
    print ( "Hvitelistet: " + json.dumps(decodedResponse ["data"]["isWhitelisted"]) + "\n")

    #This conditional statement outputs the status of the ip address based on abuse of confidence
    if json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]) == "100":
        print ( Fore.YELLOW + "IP Addressen " + sys.argv[1] + " Er ondsinnet og kjent for SSH Bruteforce Angrep" + "\n")
    elif json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]) == "0":
        print ( Fore.GREEN + "IP Addressen " + sys.argv[1] + " Er ikke ondsinnet" + "\n")
    elif json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]) < "20":
        print ( "IP Addressen " + sys.argv[1] + " Er sannsynligvis ikke ondsinnet, men bør undersøkes nærmere")
    elif json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]) <= "20":
        print ( "IP Adressen " + sys.argv[1] + " Er sannsynligvis ondsinnet og bør undersøkes nærmere")
    else:
        print ( "[*] IP-omdømmeoppslag fullført!!!" + "\n" )

    print ( Fore.GREEN + "[*] IP-omdømmeoppslag fullført!!!" + "\n" )
