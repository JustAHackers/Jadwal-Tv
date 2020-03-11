#coding: utf-8

#Silakan Dipelajari :)

import requests,bs4
# import module yg dibutuhkan

acaratv=["trans7","rcti","antv","indosiar","transtv","sctv","metrotv","gtv","mnctv","tvone","inewstv","tvri","nettv","rtv","kompastv"]
# list acara tv

for i in range(len(acaratv)):
    print ("\x1b[1;33m "+str(i+1).ljust(2)+" . \x1b[1;32m"+acaratv[i])
# Perulangan Untuk Print Menu Acara Tv

while True:
  try:
   aska=int(raw_input("\x1b[1;34mNomor > "))-1
   if aska < len(acaratv): break
  except:
   pass
# Perulangan Untuk Input 

url_to_parse=requests.get("https://www.jadwaltv.net/channel/"+acaratv[aska]).text
#melakukan request ke website jadwaltv

par=bs4.BeautifulSoup(url_to_parse,"html.parser")
par=par.findAll("td")
# Untuk Parse Html dari website jadwaltv

par=par[2:]
# Memotong 2 Isi List,Karena Isi Tersebut Bukan Termasuk dari jadwal tv 

jam=[]
acara=[]
#List Untuk Di Append

for i in range (len(par)):
    if i == 0: jam.append(par[i].text)
    elif i % 2 == 0 and par[i] not in jam: jam.append(par[i].text)
    elif i % 2 != 0 and par[i] not in jam: acara.append(par[i].text)
    #Untuk Memisahkan Antara Jam Dan Acara TV
#Perulangan Untuk Mengisi List Acara Dan Jam

print ("""
╔════╦════════════════════╦══════════╗
║ NO ║      ACARA TV      ║    JAM   ║
╠════╬════════════════════╬══════════╣""")
for i in range (len(acara)):
    if len(acara[i]) > 20: jst=acara[i][:17].ljust(20,".")
    else: jst = acara[i].ljust(20)
    print ("║ {} ║{}║ {} ║").format(str(i).ljust(2),jst,jam[i])
    #Untuk Menyesuaikan Text Agar Tidak Merusak bentuk tabel

print ("╚════╩════════════════════╩══════════╝")
#Untuk Print Hasil Dari Parse Tadi
