sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for location in sales_data:
    for amount in location:
        scoops_sold += amount
print(scoops_sold)



celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = []
for temperature_in_celsius in celsius:
    temperature_in_fahrenheit = temperature_in_celsius * 9/5 + 32
    fahrenheit.append(temperature_in_fahrenheit)
print(fahrenheit)






