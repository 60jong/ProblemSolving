left = 3120
coinCnt = 0

coin500 = left // 500
left = left - coin500 * 500

coin100 = left // 100
left = left - coin100 * 100

coin50 = left // 50
left = left - coin50 * 50

coin10 = left // 10
left = left - coin10 * 10

coinCnt = coin10 + coin50 + coin100 + coin500
print(coinCnt)
print(left)