from datetime import datetime

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = datetime.strptime(start_time, "%I %p")
    self.end_time = datetime.strptime(end_time, "%I %p")
    self.times = [self.start_time, self.end_time]
  
  def __repr__(self):
    return "We are currently serving {name} menu items from {start} until {end}.".format(name = self.name, start=self.start_time, end=self.end_time)
  
  def calculate_bill(self, purchased_items): #2 arg is a list
    total_bill = 0
    for item in purchased_items:
      total_bill += self.items.get(item, 0)
    return total_bill

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return "This location of Basta Fazzoolin can be found at {address}.".format(address = self.address)
  
  def available_menus(self, time):
    the_time = datetime.strptime(time, "%I %p")
    for menu_items in range(len(self.menus)):
      if the_time >= self.menus[menu_items].start_time and the_time <= self.menus[menu_items].end_time:
        print(self.menus[menu_items])
      
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
  
brunch = Menu("Brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, "11 AM", "4 PM")
#print(brunch.items)
#print(brunch.start_time)

early_bird = Menu("Early-bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,},"3 PM", "6 PM")

#print(early_bird.start_time)

dinner = Menu("Dinner", {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,},"5 PM","11 PM")

kids = Menu("Kids Menu", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, "11 AM","9 PM")

#print(brunch)
#print(brunch.items)
#print(brunch.calculate_bill(["pancakes", "home fries", "coffee"]))
#print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])

new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])
#print(new_installment.available_menus("12 PM"))
#print(new_installment.available_menus("5 PM"))

bus_1 = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas_menu = Menu("Take a' Arepa", {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, "10 AM", "8 PM")
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

bus_2 = Business("Take a' Arepa", [arepas_place])
