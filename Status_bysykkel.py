# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:04:02 2019

@author: HALHUS
"""

import  json, urllib.request
import pandas as pd

#Funksjon for å lese json fil fra nett.  
def les_fil(url):
    output = urllib.request.urlopen(url).read()
    x = json.loads(output)
    return x

############################################################################################
# Leser data for informasjon om stasjoner
############################################################################################
data = les_fil("https://gbfs.urbansharing.com/oslobysykkel.no/station_information.json")
antall_stasjoner = len(data["data"]["stations"]) 
Tid_stasjoner = data["last_updated"]
x = 0
Stasjoner_Liste = []
#Henter informasjon fra stasjoner som er etterspurt
while x < antall_stasjoner:
    store_details = {"name":None, "station_id":None}
    store_details['name'] = data["data"]["stations"][x]["name"]
    store_details['station_id'] = data["data"]["stations"][x]["station_id"]
    Stasjoner_Liste.append(store_details)
    x+=1

############################################################################################
# Leser data for status for stasjoner
############################################################################################
status = les_fil("https://gbfs.urbansharing.com/oslobysykkel.no/station_status.json")
antall_stasjoner = len(status["data"]["stations"]) 
Tid_status = status["last_updated"]
x = 0
Status_Liste = []
while x < antall_stasjoner:
    store_details = {"num_bikes_available":None, "station_id":None, "num_bikes_available":None}
    store_details['num_bikes_available'] = status["data"]["stations"][x]["num_bikes_available"]
    store_details['station_id'] = status["data"]["stations"][x]["station_id"]
    store_details['num_docks_available'] = status["data"]["stations"][x]["num_docks_available"]
    Status_Liste.append(store_details)
    x+=1

#Legger til informasjon fra stasjoner til status
for i, v in enumerate(Stasjoner_Liste):
    Status_Liste[i].update(v)
#Formaterer slik at listen skrives ut
pd.set_option('display.width', 200)
df = pd.DataFrame(Status_Liste)
print(df)

