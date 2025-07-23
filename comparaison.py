import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb 
import yfinance as yf

## importation de AAPL

import apple as apple 


##Comparaison multi-actifs 
## Téléchager plusieurs actions et les comparer vis a vis du prix normalisés, le rendement cumulés et la volatilité


###  TESLA 
def tesla_data(): 
    ticker2 = yf.Ticker("TSLA")
    tesla = ticker2.history(period="1y")


    tesla = tesla.reset_index()
    tesla = tesla.sort_values("Date")
    tesla['Date'] = pd.to_datetime(tesla['Date'])

    ##print(tesla.head(10))
    ## prix normalisé 
    prix_normalise = tesla['Close'].iloc[-1] / tesla['Close'].iloc[0]

    ## rendement cumulé 
    tesla['Rendement'] = tesla['Close'].diff() / tesla['Close'].shift(1)
    tesla['Facteur de croissance'] = 1 + tesla['Rendement']

    ## Volatilité 
    tesla['Volatilité sur 20j'] = tesla['Rendement'].rolling(window=20).std()

    return tesla

###  BTC-USA 
def Btc_data(): 
    ticker3 = yf.Ticker("BTC-USD")
    BTC = ticker3.history(period="1y")


    BTC = BTC.reset_index()
    BTC = BTC.sort_values("Date")
    BTC['Date'] = pd.to_datetime(BTC['Date'])

    ##print(BTC.head(10))
    ## prix normalisé 
    prix_normalise_BTC = BTC['Close'].iloc[-1] / BTC['Close'].iloc[0]

    ## rendement cumulé 
    BTC['Rendement'] = BTC['Close'].diff() / BTC['Close'].shift(1)
    BTC['Facteur de croissance'] = 1 + BTC['Rendement']

    ## Volatilité 
    BTC['Volatilité sur 20j'] = BTC['Rendement'].rolling(window=20).std()
    return BTC

apple_data = apple.analyse_apple()

def plot_comparaison(BTC,tesla,apple_data):
    plt.figure(figsize=(20,26))

    plt.subplot(2,2,1)
    plt.plot(tesla['Date'],tesla['Volatilité sur 20j'], label = "TESLA", color="blue")
    plt.plot(BTC['Date'], BTC['Volatilité sur 20j'], label="BTC", color="red")
    plt.plot(tesla['Date'], apple_data['Volatilité sur 20j'], label="Apple", color="orange")
    plt.xlabel("Date")
    plt.ylabel("Volatilité sur 20j")
    plt.title("Comparaison de la volatilté roulante(TESLA,BTC-USD,APPLE)")
    plt.legend(loc="upper left")


    plt.subplot(2,2,2)
    plt.plot(tesla['Date'],tesla['Facteur de croissance'], label = "TESLA", color="blue")
    plt.plot(BTC['Date'], BTC['Facteur de croissance'], label="BTC", color="red")
    plt.plot(tesla['Date'], apple_data['Facteur_Croissance'], label="Apple", color="orange")
    plt.xlabel("Date")
    plt.ylabel("Facteur de croissance")
    plt.title("Comparaison du facteurs de croissance(TESLA,BTC-USD,APPLE)")
    plt.legend(loc="upper left")
    plt.savefig("Comparaison.png", format='PNG')
    plt.show()