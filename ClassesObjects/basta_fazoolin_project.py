class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

class Franchise:
  def __init__(self, address, menus, rest_name):
    self.address = address
    self.menus = menus
    self.rest_name = rest_name
    
  def __repr__(self):
    return 'Our {rest_name} address is {address}'.format(rest_name = self.rest_name, address = self.address)

  def available_menus(self, time):
    available_menu = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menu.append(menu)
    return available_menu

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return 'Our {name} menu is available from {start_time} till {end_time} every day!'.format(name = self.name, start_time = self.start_time, end_time = self.end_time)

  def calculate_bill(self, purchased_items):
    bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return bill
    

items_brunch = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch = Menu("brunch", items_brunch, 1100, 1600)

print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))

items_bird = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird = Menu("early bird",  items_bird, 1500, 1800)

print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

items_dinner = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner = Menu("dinner", items_dinner, 1700, 2300)

items_kids = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids = Menu("kids", items_kids, 1100, 2100)

arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepa = Menu("Take a’ Arepa", arepas_menu, 1000, 2000)

print(brunch)

menus = [brunch, early_bird, dinner, kids]
flagship_store = Franchise("1232 West End Road", menus, "FS")
new_installment = Franchise("12 East Mulberry Street", menus, "NI")
arepas_place = Franchise("189 Fitzgerald Avenue", menus, "AP")

first_business = Business("Basta Fazoolin' with my Heart" ,[flagship_store, new_installment])

arepa = Business("Take a’ Arepa",[arepas_place])

print(flagship_store)
print(flagship_store.available_menus(1200))
print(flagship_store.available_menus(1500))

