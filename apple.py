import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_apple_data():
    ticker = yf.Ticker("AAPL")
    data = ticker.history(period="1y")
    data = data.reset_index()
    data = data.sort_values("Date")
    data['Date'] = pd.to_datetime(data['Date'])
    return data

def analyse_apple():
    df_simple = get_apple_data()[['Date','Close','Volume']]
    
    # Calculs
    df_simple['SMA_20'] = df_simple['Close'].rolling(window=20).mean()
    df_simple['Rendement Journalier(%)'] = df_simple['Close'].diff()/ df_simple['Close'].shift(1) * 100
    df_simple = df_simple.fillna(0)
    df_simple['rendement en proportion'] = df_simple['Close'].diff()/ df_simple['Close'].shift(1)
    df_simple['Facteur_Croissance'] = 1 + df_simple['rendement en proportion']
    df_simple['Indice_Croissance'] = df_simple['Facteur_Croissance'].cumprod()
    df_simple['Volatilité sur 20j'] = df_simple['rendement en proportion'].rolling(window=20).std()
    
    return df_simple

def plot_apple(df_simple):
    plt.figure(figsize=(20,26))

    # Prix et volume
    ax1 = plt.subplot(2,2,1)
    color = 'red'
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Prix de clôture', color=color)
    ax1.plot(df_simple['Date'], df_simple['Close'], color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'blue'
    ax2.set_ylabel('Volume d\'échange', color=color)
    ax2.plot(df_simple['Date'], df_simple['Volume'], color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title('Prix de clôture et volume d\'échange')

    # SMA et close
    plt.subplot(2,2,2)
    plt.plot(df_simple['Date'],df_simple['SMA_20'], label="Moyenne 20 jours",color="red")
    plt.plot(df_simple['Date'],df_simple['Close'], label="Close",color="blue")
    plt.xlabel("Date")
    plt.ylabel("Prix")
    plt.title("Moyenne mobile sur 20 jours")
    plt.legend()

    # Rendement cumulé
    plt.subplot(2,2,3)
    plt.plot(df_simple['Date'],df_simple['Indice_Croissance'])
    plt.ylabel("Indice de croissance")
    plt.xlabel("Date")
    plt.title("Evolution des rendements cumulés")

    # Volatilité
    plt.subplot(2,2,4)
    plt.bar(df_simple['Date'], df_simple['Volatilité sur 20j'], color="blue")
    plt.xlabel("Date")
    plt.ylabel("Volatilité roulante")
    plt.title("Volatilité roulante sur 20 jours")

    plt.tight_layout()

    plt.savefig("apple.png", format="PNG")
    plt.show()

def saveData(data,name_file): 
    data.to_csv(name_file,sep=';',index=False)
    print("Fichier enregistrer avec succes")