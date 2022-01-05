#pizza toppings and prices
toppings=["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms"]
prices=[2,6,1,3,2,7,2]
#welcome line, with number of pizzas avaliable
num_two_dollar_slices= prices.count(2)
print(num_two_dollar_slices)
num_pizzas=len(toppings)
print("We sell",num_pizzas,"different kinds of pizza!")

pizza_and_prices=[[2,"pepperoni"],[6,"pineapple"],[1,"cheese"],[3,"sausage"],[2,"olives"],[7,"anchovies"],[2,"mushrooms"]]
print(pizza_and_prices)
#pizza prices sorted from cheapest to most expensive
pizza_and_prices.sort()
print(pizza_and_prices)

#getting cheapest pizza price
cheapest_pizza=pizza_and_prices[0]
print(cheapest_pizza)
#getting most expensive pizza price
priciest_pizza=pizza_and_prices.pop()
print(priciest_pizza)
#getting 3 of the cheapest prices of pizza
three_cheapest=pizza_and_prices[:3]
print(three_cheapest)
