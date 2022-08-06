
coins = ["harmony","bnb","stellar","avalanche","cosmos","harmony","bnb","stellar","avalanche","cosmos"]

prices = [0.15,1.28,0.98,60.21,20.44]


coins.insert(4,"harmony")


bullish = coins.copy() + prices.copy()

print(bullish)
print(coins.count("harmony"))
