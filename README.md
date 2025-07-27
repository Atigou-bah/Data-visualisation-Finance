# 📊 Data Visualisation Financière – Analyse d'Apple, Tesla et Bitcoin

## 🎯 Objectif

Ce projet vise à démontrer et renforcer mes compétences en **analyse de données** et **visualisation en Python**, en utilisant des données financières réelles.  
L’analyse porte principalement sur **l’action Apple (AAPL)** sur une période d’un an (juillet 2024 à juillet 2025), suivie d’une **comparaison** avec **Tesla (TSLA)** et le **Bitcoin (BTC-USD)**.

---

## 🚀 Lancement du projet

1. Cloner le dépôt
2. Lancer le fichier principal (main script)
3. Les résultats sont :
   - Affichés en graphique
   - Sauvegardés dans des fichiers `.csv` et `.png`

---

## 🧪 Analyse des données

L’analyse a été menée en deux temps :

### 1. Analyse d'Apple (AAPL)
- **Exploration** :
  - Prix de clôture et volume d’échange
  - Moyenne mobile sur 20 jours (SMA 20)
- **Performance** :
  - Rendement journalier (%) et rendement cumulé
  - Indice de croissance (facteur de croissance cumulé)
- **Volatilité** :
  - Écart-type roulante sur 20 jours

### 2. Comparaison multi-actifs
Comparaison graphique des **trois actifs (AAPL, TSLA, BTC)** selon :
- Leurs **facteurs de croissance cumulés**
- Leur **volatilité roulante sur 20 jours**

---

## 📈 Visualisations

Des visualisations claires ont été générées avec `matplotlib` :

- 📉 Graphique du **prix de clôture + SMA 20**
- 📦 **Volume d’échange**
- 📊 **Rendement cumulé** (Indice de croissance)
- 🔄 **Volatilité roulante**
- ⚖️ **Comparaison** multi-actifs (volatilité et croissance)

> Tous les graphiques sont automatiquement générés à l’exécution et sauvegardés au format `.png`.

---

## 🛠️ Technologies utilisées

- **Langage** : Python 3.x  
- **Librairies** :
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `yfinance`

---


## ✅ Conclusion

Ce projet m’a permis de :
- Approfondir mes compétences en **analyse financière**
- Visualiser efficacement des **indicateurs clés**
- Manipuler des données boursières **multi-actifs** (actions, cryptomonnaies)

---

## ✨ Idées d’amélioration (future work)

- Ajouter d’autres indicateurs techniques (ex. RSI, MACD)
- Comparer sur différentes périodes (1 mois, 6 mois, 5 ans)
- Intégrer une interface utilisateur simple
