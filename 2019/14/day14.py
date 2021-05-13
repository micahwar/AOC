import math
with open("input.txt", "r") as f:
    data = f.read().split("\n")[:-1]
data = """9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL""".split("\n")

recipes = {}

for recipe in data:
    recipes[recipe.split("=")[1][4:].strip()] = [recipe.split("=")[1][2:4].strip(), [tuple(x.strip().split(" ")) for x in recipe.split("=")[0].split(",")]]

print(recipes)
totals = {}
leftOvers = {}
def getCost(Chemical, t):
   print("\nStarting Function...")
   global leftOvers
   inTotals = t
   
   numberOfDesired = int(recipes[Chemical][0])
   reactants = recipes[Chemical][1]

   needed = dict([x[::-1] for x in reactants])
   print("Needed: ", needed)
   print("Totals bought: ", inTotals)
   print("Leftovers: ", leftOvers)
   
   if not reactants[0][1] == 'ORE':
      
      
      for x in range(numberOfDesired):
         for reactant in reactants:
            
            ratio = math.ceil(int(reactant[0])/int(recipes[reactant[1]][0]))
            reactantsOfReactant = recipes[reactant[1]][1]
            if reactantsOfReactant[0][1] == 'ORE':
               if reactant[1] in leftOvers:
                  if leftOvers[reactant[1]] >= int(reactant[0]):
                     leftOvers[reactant[1]] -= int(reactant[0])
                     continue
               if not reactant[1] in inTotals:
                  inTotals[reactant[1]] = int(recipes[reactant[1]][0]) * ratio
                  if (int(recipes[reactant[1]][0]) * ratio) > int(reactant[0]):
                     leftOvers[reactant[1]] = (int(recipes[reactant[1]][0]) * ratio) - int(reactant[0])
               else:
                  inTotals[reactant[1]] += int(recipes[reactant[1]][0]) * ratio
                  if (int(recipes[reactant[1]][0]) * ratio) > int(reactant[0]):
                     if reactant[1] in leftOvers:
                        leftOvers[reactant[1]] += (int(recipes[reactant[1]][0]) * ratio) - int(reactant[0])
                     else:
                        leftOvers[reactant[1]] = (int(recipes[reactant[1]][0]) * ratio) - int(reactant[0])
            else:
               if not reactant[1] in leftOvers:
                  if (int(recipes[reactant[1]][0]) * ratio) > int(needed[reactant[1]]):
                     leftOvers[reactant[1]] = (int(recipes[reactant[1]][0]) * ratio) - int(needed[reactant[1]])
               else:
                  if leftOvers[reactant[1]] >= int(needed[reactant[1]]):
                     leftOvers[reactant[1]] -= int(needed[reactant[1]])
                     continue
                  else:
                     if (int(recipes[reactant[1]][0]) * ratio) > int(needed[reactant[1]]):
                        leftOvers[reactant[1]] += (int(recipes[reactant[1]][0]) * ratio) - int(needed[reactant[1]])
               for x in range(ratio):
                  inTotals = getCost(reactant[1], inTotals)
   return inTotals


totals = getCost('FUEL', totals)
totalCost = 0
inPos = {}
for chemical in totals:
    if recipes[chemical][1][0][1] == 'ORE':
        rounded = math.ceil(totals[chemical] / int(recipes[chemical][0]))
        totalCost += int(recipes[chemical][1][0][0]) * rounded
        inPos[chemical] = int(recipes[chemical][1][0][0]) * rounded
print("Totals: ", totals)
print("Cost: ", inPos)
print("Total Cost: ", totalCost)
