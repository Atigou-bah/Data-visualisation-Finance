import apple as apple
import comparaison as cmp


apple_data = apple.analyse_apple()
btc_data = cmp.Btc_data()
tesla_data = cmp.tesla_data()

## L'étude complète de Apple 
apple.plot_apple(apple_data)

## Comparaison 
cmp.plot_comparaison(btc_data,tesla_data,apple_data)