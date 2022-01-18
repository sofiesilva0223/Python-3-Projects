hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price=0

for money in prices:
  total_price+=money
  print(total_price)


#avg hair cut cost
average_price = total_price/len(prices)
print("The average cost of a haircut is",average_price)

#reduce cost by $5
new_prices = [discount-5 for discount in prices]
print("New Prices:",new_prices)

#total revenue
total_revenue=0
for i in range(len(hairstyles)):
  total_revenue+=prices[i]*last_week[i]
print("Total Revenue:",total_revenue)

#avg daily revenue
average_daily_revenue=total_revenue/7
print(average_daily_revenue)

#advertising haircuts under $30
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if prices[i]<30]
print(cuts_under_30)
