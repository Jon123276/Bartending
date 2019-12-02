# Array
Serial = raw_input("Input the full SN: ")
# Dictoionaries
color_map = {
  "red": "Adelhyde",
  "green": "Flanergide",
  "yellow": "Bronson ext",
  "white": "Karmotrine",
  "blue": "Powdered delta"
}
ingredients_number = {
  "Adelhyde": 3,
  "Powdered delta": 1,
  "Flanergide": 2,
  "Bronson ext": 4,
  "Karmotrine": 5
}
patron_map = {
  0: "Barbara",
  1: "Patricia",
  2: "Karl",
  3: "Konrad",
  4: "Vivi",
  5: "Angelika",
  6: "Donna",
  7: "Gabe",
  8: "Clayton",
  9: "Chip"
}
# Table
drink_preferences = {
  "Barbara": "Blue Fairy,Piano Man,Frothy Water,Piano Woman,Fringe Weaver,Absinthe".split(","),
  "Patricia": "Frothy Water,Piano Woman,Fringe Weaver,Grizzly Temple,A Fedora,Rum,".split(","),
  "Karl": "Piano Man,Rum,Grizzly Temple,Mulan Tea,Absinthe,Frothy Water,".split(","),
  "Konrad": "Mulan Tea,Frothy Water,Fluffy Dream,Bleeding Jane,Rum,A Fedora".split(","),
  "Vivi": "Fluffy Dream,Moonblast,Absinthe,Piano Man,Beer,Fringe Weaver,".split(","),
  "Angelika": "Piano Woman,Blue Fairy,A Fedora,Absinthe,Bleeding Jane,Grizzly Temple".split(","),
  "Donna": "Beer,Sugar Rush,Piano Woman,Bloom Light,Moonblast,Mulan Tea".split(","),
  "Gabe": "Moonblast,Mulan Tea,Sugar Rush,A Fedora,Frothy Water,Bloom Light".split(","),
  "Clayton": "Grizzly Temple,Bloom Light,Bleeding Jane,Fringe Weaver,Piano Man,Beer".split(","),
  "Chip": "Bleeding Jane,Grizzly Temple,Moonblast,Sugar Rush,Blue Fairy,Fluffy Dream".split(",")
}


# End of Ingredients
ingredients = [color_map[raw_input("Input a color: ")] for i in range(5)]
numbers = [ingredients_number[i] for i in ingredients]
# Patron
patron = patron_map[((numbers[0]*2)+numbers[1]) % 10]
# Drink
drinkValue = ((numbers[3]*2) + numbers[4]) % 7
if (drinkValue == 0):
  drinkValue = 1
# Drink stuff
print "Your patron is", patron
print "Your drink value is", drinkValue
print "Your drink is", drink_preferences[patron][drinkValue - 1], ". Check the ingredients for this drink"

def print_ingredients(drink):
  if (drink_preferences[patron][drinkValue - 1] not in ["A Fedora", "Mulan Tea", "Absinthe", "Rum"]):
    multiplier = 1
    for f in Serial:
      if f in 'B1G':
        print "Doubling ingredients..."
        multiplier = 2
        break
    for i in range(5):
      print ingredients[i], '=', numbers[i] * multiplier
  else:
    print "Pick the bottled drink: ", drink_preferences[patron][drinkValue - 1]

common_chars = 0
for c in Serial:
  if c in 'CH4S3R':
    common_chars += 1
if (common_chars >= 3):
  print "Do two drinks, first drink is above and second is", drink_preferences[patron][(drinkValue - 1 + numbers[2]) % 6]
print "Your first drink contains: \n", print_ingredients(drink_preferences[patron][(drinkValue - 1)])
if (common_chars >= 3):
  print "Your second drink is \n", print_ingredients(drink_preferences[patron][(drinkValue - 1 + numbers[2]) % 6])
