#Tramite questo script l'utente può specificare un indirizzo di una pagina XML contenente i bandi e le gare di una PA. 
#Il codice si preoccupa di costruire la relativa tabella csv del file XML indicato.

import pandas as pd
import itertools
from bs4 import BeautifulSoup
import requests

#Inserimento indirizzo file XML da parte dell'utente
url = input("Inserisci URL file XML: ")

#Recuperiamo la pagina XML indicata
r = requests.get(url)

#Costruiamo un oggetto di tipo BeautifulSoup
soup = BeautifulSoup(r.text, "html.parser")

cig =  [ values.text for values in soup.findAll("cig")]
denominazione =  [ values.text for values in soup.findAll("denominazione")]
oggetto =  [ values.text for values in soup.findAll("oggetto")]
sceltaContraente = [ values.text for values in soup.findAll("sceltaContraente")]
importoAggiudicazione = [ values.text for values in soup.findAll("importoAggiudicazione")]

data = [item for item in itertools.zip_longest(cig, importoAggiudicazione, denominazione, sceltaContraente, oggetto)]
df  = pd.DataFrame(data=data)

#Stampo il dataframe costruito
print(df)

#Genero un file csv e lo salvo in locale
df.to_csv("sample.csv",index=False, header=None)
