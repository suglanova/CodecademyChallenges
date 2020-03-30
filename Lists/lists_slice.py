 toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]
num_pizzas = len(toppings)
x = num_pizzas
print("We sell " + str(x) + " different kinds of pizza!")
pizzas = list(zip(toppings, prices))
print(pizzas)

pizzas.sort(key = lambda x: x[1])
cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]
three_cheapest = pizzas[0:3]
print(three_cheapest)
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)


#We sell 7 different kinds of pizza!
#[('pepperoni', 2), ('pineapple', 6), ('cheese', 1), ('sausage', 3), ('olives', 2), ('anchovies', 7), ('mushrooms', 2)]
#[('cheese', 1), ('pepperoni', 2), ('olives', 2)]
#3