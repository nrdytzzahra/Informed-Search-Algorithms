import pandas as pd
import numpy as np
import warnings
import sys
warnings.simplefilter(action='ignore', category=FutureWarning)

from google.colab import drive
drive.mount('/content/drive')

from google.colab import drive
import csv
data = pd.read_csv('data.csv')

heuristik = data.heuristik.values
heuristik

jarak = data.jarak.values
jarak

def a_start(start, akhir):
  kota = []
  visit = 0
  kota.append(start)
  while kota[-1] != akhir :
    print(kota[-1],':')
    kota_tetangga = data[data['Tetangga']== kota[-1]].copy()
    kota_tetangga['fn'] = kota_tetangga['heuristik']+kota_tetangga['jarak']+visit
    kota_terdekat=kota_tetangga.loc[kota_tetangga['fn'].idxmin(),'Nama Kota']
    for tetangga in kota_tetangga['Nama Kota']:
      print(tetangga)

    kota.append(kota_terdekat)
    print(kota,'\n')
  return kota
  
  path = a_start('Arad','Bucharest')
