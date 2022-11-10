import numpy as np
import pandas as pd
import sys
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from google.colab import drive
drive.mount('/content/drive')

from google.colab import drive
import csv
Data = pd.read_csv('Data_Romania.csv')

Nilai_Heuristik = Data.Nilai_Heuristik.values

Nilai_Jarak = Data.Nilai_Jarak.values

def a_star(start, finish):
  city = []
  visit = 0
  city.append(start)
  while city[-1] != finish :
    print(city[-1],':')
    neighbor_city = Data[Data['Kota Tetangga']== city[-1]].copy()
    neighbor_city['fn'] = neighbor_city['Nilai_Heuristik']+neighbor_city['Nilai_Jarak']+visit
    nearest_city=neighbor_city.loc[neighbor_city['fn'].idxmin(),'Nama Kota']
    for tetangga in neighbor_city['Nama Kota']:
      print(tetangga)

    city.append(nearest_city)
    print(city,'\n')
  return city
  
path = a_star('Oradea', 'Bucharest')
