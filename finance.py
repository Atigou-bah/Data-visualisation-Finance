import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb 
import yfinance as yf


## 1. Téléchargement des données financières (APPLE) 

ticker = yf.Ticker("AAPL")
data = ticker.history(period="1y")

print(data.head())

# Conversion de la date 
data = data.reset_index()
data = data.sort_values("Date")
data['Date'] = pd.to_datetime(data['Date'])


## 2. Analyse exploratoire 
## 2.1 visualisation des prix de clôtures et les volumes d'échange pour les differentes dates 
df_simple = data[['Date','Close','Volume']]
df_simple = df_simple.sort_values('Date')
##print(df_simple.head(10))
plt.figure(figsize=(20,26))
ax1 = plt.subplot(2,2,1)

# Axe pour le prix de clôture
color = 'red'
ax1.set_xlabel('Date')
ax1.set_ylabel('Prix de clôture', color=color)
ax1.plot(df_simple['Date'], df_simple['Close'], color=color, label='Prix de clôture')
ax1.tick_params(axis='y', labelcolor=color)
ax1.legend(loc="upper left")

# Deuxième axe Y pour le volume
ax2 = ax1.twinx()
color = 'blue'
ax2.set_ylabel('Volume d\'échange', color=color)
ax2.plot(df_simple['Date'], df_simple['Volume'], color=color, label='Volume d\'échange')
ax2.tick_params(axis='y', labelcolor=color)
ax2.legend(loc="upper right")

# Titre et affichage
plt.title('Visualisation du prix de clôture et du volume d\'échanges')
plt.grid(True)


## 2.2 la moyenne mobile sur 20 jours SMA
df_simple['SMA_20'] = df_simple['Close'].rolling(window=20).mean()

plt.subplot(2,2,2)


plt.plot(df_simple['Date'],df_simple['SMA_20'], label="Moyenne",color="red")
plt.plot(df_simple['Date'],df_simple['Close'], label="Close",color="blue")
plt.xlabel("Date")
plt.ylabel("Moyenne_20/Close")
plt.title("Moyenne SMA")


## 3 Analyse des performances 
## 3.1 Rendement journaliers 
df_simple['Rendement Journalier(%)'] = df_simple['Close'].diff()/ df_simple['Close'].shift(1) * 100
df_simple = df_simple.fillna(0) # mettre les valeurs Nan à 0
print(df_simple.head(10))

## 3.2 Rendement Total 

prix_initial = data['Close'].iloc[0]
prix_final = data['Close'].iloc[-1]

dividendes_total = data['Dividends'].sum()

rendement_total = ((prix_final - prix_initial + dividendes_total) / prix_initial) * 100
print(f"Rendement total sur 1 an : {rendement_total:.2f} %")

## 3.1 Graphe de l'évolution des rendements cumulés 
df_simple['rendement en proportion'] = df_simple['Close'].diff()/ df_simple['Close'].shift(1)
df_simple['Facteur_Croissance'] = 1 + df_simple['rendement en proportion']  # facteur = 1 + rendement
df_simple['Indice_Croissance'] = df_simple['Facteur_Croissance'].cumprod()   # produit cumulé en pourcentage 

plt.subplot(2,2,3)
plt.plot(df_simple['Date'],df_simple['Indice_Croissance'])
plt.ylabel("Indice de croissances")
plt.xlabel("Date")

plt.title("Evolution des rendements cumulés")
print(df_simple.head(30))
plt.savefig("Graphique.png",format="PNG")
plt.show()






