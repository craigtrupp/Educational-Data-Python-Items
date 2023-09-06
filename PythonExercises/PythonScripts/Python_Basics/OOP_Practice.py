# define a basic city class
class City:
    name = ""
    country = ""
    elevation = 0 
    population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
# Initialize the variable that will hold 
# the information of the city with 
# the highest elevation 
    return_city = City()

    # Evaluate the 1st instance to meet the requirements:
    # does city #1 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city1.population > min_population and min_population < city2.population and min_population < city3.population:
        if city1.elevation > city2.elevation and city1.elevation > city3.elevation:
            return_city = city1

    # Evaluate the 2nd instance to meet the requirements:
    # does city #2 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city2.population > min_population and min_population > city1.population and min_population < city3.population:
        if city2.elevation > city3.elevation:
            return_city = city2

    # Evaluate the 3rd instance to meet the requirements:
    # does city #3 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city3.population > min_population and min_population >city2.population and min_population > city1.population:
        return_city = city3

    #Format the return string
    if return_city.name:
        return f'{return_city.name}, {return_city.country}'
    else:
        return ""

print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""

## Printouts
# Cusco, Peru
# Sofia, Bulgaria



class Furniture:
	color = ""
	material = ""

table = Furniture()
table.color = 'brown'
table.material = 'wood'

couch = Furniture()
couch.color = 'red'
couch.material = 'leather'

def describe_furniture(piece):
	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

print(describe_furniture(table)) 
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch)) 
# Should be "This piece of furniture is made of red leather"

## Printouts
# This piece of furniture is made of brown wood
# This piece of furniture is made of red leather



# Finish the "Stock_by_Material" method and iterate over the amount of each item of a given material that is in stock. When you’re finished, the script should add up to 10 cotton clothing items.
class Clothing:
  stock={ 'name': [],'material' :[], 'amount':[]}
  def __init__(self,name):
    material = ""
    self.name = name
  def add_item(self, name, material, amount):
    self.stock['name'].append(self.name)
    self.stock['material'].append(self.material)
    self.stock['amount'].append(amount)
  def Stock_by_Material(self, material):
    count=0
    n=0
    for item in self.stock['material']:
      if item == material:
        count += self.stock['amount'][n]
        n+=1
    return count

class shirt(Clothing):
  material="Cotton"
class pants(Clothing):
  material="Cotton"
  
polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)

## Here is your output: 10

## Nice job! You successfully used composition to reuse the Clothing.stock attribute and stock_by_material() function of
## the Clothing class to take stock of the Cotton shirts and pants!