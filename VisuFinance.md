# Projet d'Analyse Financière avec Python

## Objectif du projet
Analyser les données financières d’une ou plusieurs actions (ou cryptomonnaies) en utilisant Python. Visualiser les prix, les tendances, la volatilité et les performances.

---

## Tâches principales

### 1. Préparation du projet
- Installer Python et les bibliothèques nécessaires :
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `yfinance` (pour télécharger les données financières)
  - (optionnel) `plotly` pour les graphes interactifs

---

### 2. Téléchargement des données financières
- Choisir une ou plusieurs actions (ex : AAPL, TSLA, BTC-USD).
- Télécharger les données historiques via Yahoo Finance avec la bibliothèque `yfinance`.
- Filtrer la période souhaitée (ex : dernières 2 années).

---

### 3. Analyse exploratoire
- Visualiser :
  - Prix de clôture.
  - Volume d’échange.
- Calculer :
  - Moyenne mobile sur 20 jours.
  - Moyenne mobile sur 50 jours.

---

### 4. Visualisation des tendances
- Graphe prix de clôture + moyennes mobiles.
- Graphe volume d’échange.

---

### 5. Analyse des performances
- Calculer les **rendements journaliers**.
- Calculer le **rendement total** (depuis le début de la période).
- Graphe de l’évolution des rendements cumulés.

---

### 6. Analyse de la volatilité
- Calculer l’**écart-type** des rendements (volatilité).
- Visualiser la **volatilité roulante** (sur 20 jours).
- Graphe volatilité.

---

### 7. Comparaison multi-actifs
- Télécharger plusieurs actions simultanément.
- Comparer :
  - Prix normalisés.
  - Rendements cumulés.
  - Volatilité.

---

### 8. Export des résultats
- Exporter les données finales (prix, moyennes, volatilité, rendements) dans un fichier CSV ou Excel.
- Enregistrer les graphiques (format PNG ou PDF).

---

### 9. Idées bonus
- Interface graphique avec Streamlit ou Dash.
- Tableau de bord interactif avec Plotly.
- Automatisation : script qui met à jour les données chaque jour.

---

> 💡 **Conseil :** Avance étape par étape et consulte la documentation officielle des bibliothèques.
